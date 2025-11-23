// pipeline {
//     agent any

//     // 全局配置
//     options{
//         timestamp()
//         timeout(time:10, unit:'MINUTES')
//     }

//     // 环境变量
//     enviornment{
//         VENV_BIN = "${WORKSPACE}/venv/bin"
//     }

//     // 
//     stages {
//         stage('Hello') {
//             steps {
//                 echo 'Jenkinsfile found! Build is successful.'
//             }
//         }
//     }
// }

pipeline {
    agent any
    stages {
        stage('Check Python') {
            steps {
                script {
                    try {
                        // 尝试打印版本号
                        sh 'python3 --version'
                        echo "✅ 检测成功：Python3 已安装"
                    } catch (Exception e) {
                        echo "❌ 检测失败：未找到 python3 命令"
                        // 可以在这里让流水线报错停止
                        error("请在 Jenkins 节点上安装 Python3")
                    }
                }
            }
        }
    }
}