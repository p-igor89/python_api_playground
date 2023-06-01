node {
    stage('Checkout repo') {
        git branch: 'main',
        credentialsId: 'e047276c-9e29-460a-9cd5-27aec0be5fd3',
        url: 'https://github.com/p-igor89/python_api_playground.git'
    }
    stage('Install Python') {
        sh 'pip install python3'
    }
    stage('Install deps') {
        sh 'pipenv install'
    }
    stage('Test') {
        sh 'pipenv run pytest tests -sv --alluredir=allure-results'
    }
    stage('Report') {
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
