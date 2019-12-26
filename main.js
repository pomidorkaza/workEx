const { app, BrowserWindow} = require('electron');

let window;

const { PythonShell } =  require('python-shell');

PythonShell.run('index.py',(err,res)=>{

});
function createWindow(){

    window = new BrowserWindow({width: 800, height: 600});

    window.loadURL('http://localhost:8881');
    
  
 }

app.on('ready', createWindow);
