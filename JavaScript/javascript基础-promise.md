## 期约与异步函数

ECMAScript 6 新增了正式的 Promise（期约）引用类型，支持优雅地定义和组织异步逻辑。之后用 ECMAScript 6 新增了正式的 Promise（期约）引用类型，支持优雅地定义和组织异步逻辑。

在 JavaScript 这种单线程事件循环模型中,异步行为是为了优化因计算量大而时间长的操作.

**异步操作并不一定计算量大或要等很长时间** 在任何你不想为等待某个异步操作而阻塞线程执行的时候都可以去使用

在 javascript 中异步行为类似于系统中断，即当前进程外部的实体可以触发代码执行。异步代码不容易推断。开始执行后,就对运行时相当于一个黑盒,无法保证执行的时间.所以需要一个**通知机制**,通知使用该变量的代码. 而无关的代码就可以直接执行.

最初之前一直是使用回调函数,如果是复杂的情况会有回调的回调,最终成为无法维护的回调地狱.

### 期约是对尚不存在结果的一个替身。

1. 使用 new 去实例化 Promise 类型.必须提供一个 executor(执行器)作为参数.
   `let p = new Promise(() => {});`
   不传就会报:
   `caught TypeError: Promise resolver undefined is not a function`

executor(执行器)有两个作用.

1. 初始化期约的异步行为
2. 控制状态的最终转换

执行器函数是同步执行的,状态转换是一次性的,无法后续再继续使用.会静默失败,所以为避免期约卡在待定状态，可以添加一个定时退出功能。比如，可以通过 setTimeout 设置一个10 秒钟后无论如何都会拒绝期约的回调. 如果已经变过了就不会在变了.

``