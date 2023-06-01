node {
    stage('Checkout repo') {
        git branch: 'main',
        credentialsId: 'e047276c-9e29-460a-9cd5-27aec0be5fd3',
        url: 'https://github.com/p-igor89/python_api_playground.git'
    }
    stage('Install pyenv and Python') {
        sh '''
            curl https://pyenv.run | bash
            echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
            echo 'eval "$(pyenv init -)"' >> ~/.bashrc
            echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
            source ~/.bashrc
            pyenv install --list | grep -v - | tail -1 | xargs pyenv install
            pyenv global $(pyenv versions --bare | tail -1)
        '''
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
