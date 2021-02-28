
class Thenable {
  constructor(num) {
    this.num = num
  }

  then(resolve, reject) {
    resolve(this.num * 2)
  }
}

// new Promise(resolve => resolve(2))
//   .then(res => {
//     console.log('yello')
//     return new Thenable(res)
//   })
//   .then(console.log)

new Promise(resolve => resolve(2))
  .then(res => console.log(res))
  .then(res => console.log(res + 'should break'))

function promisify(f) {
  return function(...args) {
    return new Promise((resolve, reject) => {
      function callback(err, result) {
        if (err) {
          reject(error)
        } else {
          resolve(result)
        }
      }

      args.push(callback)
      f.call(this, ...args)
    })
  }
}