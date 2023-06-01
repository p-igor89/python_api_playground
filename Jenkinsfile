node {
    stage('Checkout repo'){
        git branch: 'main',
        credentialsId: '5f6c5fab-317c-4294-9373-37615052c667',
        url: 'https://github.com/p-igor89/python_api_playground.git'
    }
    stage('Install deps') {
        sg 'pipenv install'
    }
    stage('Test') {
        sh 'pipenv run pytest tests -sv --alluredir-allure-results'
    }
    stage('Report'){
        script {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure_results']]
                ])
        }
    }
}