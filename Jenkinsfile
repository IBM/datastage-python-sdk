#!groovy

def GH_CREDS = '2c69d250-a91e-4941-a11b-b4c831b59b90'
//slackChannel = 'ds-nextgen-'
//slackTeamDomain = 'ibm-analytics'
//slackTokenCredentialId = '1d960160-45e6-48fe-a99c-66c1e25b4ced'

properties([
   buildDiscarder(logRotator(artifactDaysToKeepStr: '5', artifactNumToKeepStr: '5', daysToKeepStr: '5', numToKeepStr: '5'))
])
pipeline {

  agent {
    label 'ds_worker'
  }

  options {
    skipDefaultCheckout()
  }

  stages {
    stage('Checkout') {
      steps {
        withCredentials([usernamePassword(credentialsId: GH_CREDS, passwordVariable: 'GH_CREDS_PSW', usernameVariable: 'GH_CREDS_USR')]) {
        script {
          defaultInit()
          applyCustomizations()
          checkoutResult = checkout scm
          //checkourResult = checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: GH_CREDS, url: 'https://github.com/IBM/datastage-java-sdk.git']]])
          //commitHash = "${checkoutResult.GIT_COMMIT[0..6]}"
            sh '''
              #git config --global user.email $GH_SDKS_AUTOMATION_MAIL
              git config --global user.name ${GH_CREDS_USR}
              git config --global credential.username ${GH_CREDS_USR}
              git config --global credential.helper "!f() { echo password=${GH_CREDS_PSW}; echo; }; f"
              set +e
                pip3 install --upgrade bump2version
                python3 --version
              set -e
            '''
          }
        }
      }
    }//checkout

    stage('Publish[repository]') {
      when {
        beforeAgent true
        allOf {
          // Publish master branch, but not on the version update commit after just publishing
          branch 'main'
          not {
            changelog 'Update version *'
          }
        }
      }
      steps {
        withCredentials([usernamePassword(credentialsId: 'ab3252ae-4fc8-4108-8239-f61afc11ab13', passwordVariable: 'TWINE_PASSWORD', usernameVariable: 'TWINE_USERNAME'),
                         ]) {
          // Throw away any temporary version changes used for stage/test
          sh 'git reset --hard'
          bumpVersion(false)
          // Push the version bump and release tag
          sh 'git push --tags origin HEAD:main'
          //publishPublic()
          sh'''
              python3 -m pip install --upgrade pip setuptools twine
              python3 -m build
              python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*  --username ${TWINE_USERNAME} --password ${TWINE_PASSWORD} --verbose
          '''
          //publishDocs()
        }
      }
    }//publish repository
  }
}

def libName
def commitHash
def bumpVersion
def customizeVersion
def prefixSdkVersion

void defaultInit() {
  // Default to using bump2version
  bumpVersion = { isDevRelease ->
    newVersion = getNextVersion(isDevRelease)
    // Set an env var with the new version
    env.NEW_SDK_VERSION = newVersion
    doVersionBump(isDevRelease, newVersion)
  }

  doVersionBump = { isDevRelease, newVersion, allowDirty ->
    sh "/home/jenkins/.local/bin/bump2version --new-version ${newVersion} ${allowDirty ? '--allow-dirty': ''} ${isDevRelease ? '--no-commit' : '--tag --tag-message "Release {new_version}"'} patch"
  }

  getNextVersion = { isDevRelease ->
    // Identify what the next patch version is
    patchBumpedVersion = sh returnStdout: true, script: '/home/jenkins/.local/bin/bump2version --list --dry-run patch | grep new_version=.* | cut -f2 -d='
    // Now the customized new version
    return getNewVersion(isDevRelease, patchBumpedVersion)
  }

  // Default no-op implementation to use semverFormatVersion
  customizeVersion = { semverFormatVersion ->
    semverFormatVersion
  }
}

String getNewVersion(isDevRelease, version) {
  wipVersion = ''
  if (isDevRelease) {
    // Add uniqueness and build metadata to dev build versions
    wipVersion = "${version.trim()}-dev${currentBuild.startTimeInMillis}+${commitHash}.${currentBuild.number}"
  } else {
    wipVersion = "${version.trim()}"
  }
  // Customize with lang specific requirements
  return customizeVersion(wipVersion)
}

// Language specific implementations of the methods:
// applyCustomizations()
// runTests()
// publishStaging()
// publishPublic()
// publishDocs()
// + other customizations
void applyCustomizations() {
  libName = 'python'
  customizeVersion = { semverFormatVersion ->
    // Use a python format version
    semverFormatVersion.replace('-a','a').replace('-b','b').replace('-','.')
  }
}
