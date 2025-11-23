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
    // 关键修改：指定使用 python 3.9 的镜像
    agent any
    
    stages {
        stage('Check Python') {
            steps {
                // 这里的 python 命令是在容器里运行的，所以一定有
                sh 'python3 --version'
                sh 'pip install requests' // 甚至不需要 venv，因为容器是临时的
            }
        }
    }
}