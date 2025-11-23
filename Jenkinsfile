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

// pipeline {
//     agent any
//     stages {
//         stage('Check Python') {
//             steps {
//                 script {
//                     try {
//                         // 尝试打印版本号
//                         sh 'python3 --version'
//                         echo "✅ 检测成功：Python3 已安装"
//                     } catch (Exception e) {
//                         echo "❌ 检测失败：未找到 python3 命令"
//                         // 可以在这里让流水线报错停止
//                         error("请在 Jenkins 节点上安装 Python3")
//                     }
//                 }
//             }
//         }
//     }
// }

pipeline {
    agent any

    environment {
        VENV_BIN = "${WORKSPACE}/venv/bin"
    }

    stages {
        // 阶段一：环境准备
        stage('Setup') {
            steps {
                // 1. 创建虚拟环境
                sh 'python3 -m venv venv'
                // 2. 安装依赖 (此时 requirements.txt 已经通过 Git 拉下来了)
                sh "${VENV_BIN}/pip install -r requirements.txt"
            }
        }

        // 阶段二：代码检查
        stage('Lint') {
            steps {
                // 直接检查仓库里的代码文件
                sh "${VENV_BIN}/pylint main.py || true"
            }
        }

        // 阶段三：运行
        stage('Run') {
            steps {
                // 直接运行仓库里的脚本
                sh "${VENV_BIN}/python main.py"
            }
        }
    }

    post {
        always {
            // 清理虚拟环境
            sh 'rm -rf venv'
            cleanWs()
        }
    }
}