pipeline {
    agent any  // 选择任意可用的Jenkins节点执行
    tools {
        python "Python3.13.5"  // Jenkins全局工具配置的Python版本（需提前配置）
    }
    stages {
        // 阶段1：拉取代码（从Git仓库克隆）
        stage('拉取代码') {
            steps {
                git 'https://github.com/zhoudan123456/jenkins-python-allure-demo.git'  // 替换为你的仓库地址
            }
        }

        // 阶段2：安装依赖（Python包）
        stage('安装依赖') {
            steps {
                sh 'python -m pip install --upgrade pip'  // 升级pip
                sh 'pip install -r requirements.txt'     // 安装依赖
            }
        }

        // 阶段3：运行测试（生成Allure结果文件）
        stage('运行测试（生成Allure结果）') {
            steps {
                sh 'pytest --alluredir=allure-results tests/'  // 执行测试，结果输出到allure-results目录
            }
        }

        // 阶段4：生成Allure可视化报告
        stage('生成Allure报告') {
            steps {
                script {
                    // 调用Allure Jenkins插件生成报告
                    allure([
                        resultsDir: 'allure-results',  // 对应测试结果目录
                        reportBuildPolicy: 'ALWAYS'    // 始终生成报告（成功/失败都生成）
                    ])
                }
            }
        }
    }

    // 测试结果通知（成功/失败分别通知）
    post {
        success {
            emailext(
                subject: "Jenkins构建成功：${JOB_NAME} #${BUILD_NUMBER}",
                body: "构建成功！Allure报告地址：${BUILD_URL}allure",  // 报告链接
                to: "572038908@qq.com, 445561203@qq.com"  // 替换为实际收件邮箱
            )
        }
        failure {
            emailext(
                subject: "Jenkins构建失败：${JOB_NAME} #${BUILD_NUMBER}",
                body: "构建失败！日志地址：${BUILD_URL}console",  // 控制台日志链接
                to: "572038908@qq.com, 445561203@qq.com"
            )
        }
    }
}