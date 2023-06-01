const {spawn} = require('child_process')
const express = require('express')

const app = express()

app.get("/question", async (req, res) => {
    const childpython = await spawn('python',['test.py','what are renewable resources'])
    childpython.stdout.on('data',(data) =>{
        console.log(`stdout : ${data}`)
        var buf = Buffer.from(data,'utf8')
        res.json({data: buf.toString()})
    },
    childpython.stderr.on('data',(data) =>{
        console.error(`stderr : ${data}`)
        res.json({data: data})
    }),
    childpython.on('data',(data) =>{
        console.log(`exited : ${data}`)
        res.json({data: data})
    })
    )
})

app.listen(6969, () => console.log(`Port:6969`))
