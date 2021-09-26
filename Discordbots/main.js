const Bot = require('discord.js');
const fetch = require("node-fetch");
const fs = require('fs');
const { isNull } = require('util');

const client = new Bot.Client();
const prefix = '=';

var IP = '';
var address = 'https://api.mcsrvstat.us/2/'+IP;
//https://api.mcsrvstat.us/2/147.135.97.90:25620
console.log(address);

client.once('ready', ()=>{
    console.log('Online');
});

function bouy(){

}

client.on('message', message=>{

    if(!message.content.startsWith(prefix) || message.author.bot){

        if(message.member.roles.cache.some(r => r.name === "shironeko")){

            if(message.channel.name !== "general" && message.content === '>rs'){
                setTimeout(function(){message.channel.send(">c whitecat")}, 4000);
                
            }
            
        }

        return;
    }
    
    const content = message.content;
    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();

    if (command === 'online'){

        if (IP === ''){
            message.channel.send('No IP Set');
            return
        }

        fetch('https://api.mcsrvstat.us/2/147.135.97.90:25620').then(res => res.json()).then((out) => {message.channel.send('Online:' + out['players']['online']+out['players']['list']);})
       
    }else if (command === 'set'){     

        IP = content.replace(prefix+'set ', '');
        address = 'https://api.mcsrvstat.us/2/'+IP;
        message.channel.send('set IP to ' + IP);
        console.log(address);

    }else if(command === 'ip'){

        message.channel.send(IP);

    }else if (command === 'ping'){
        message.channel.send('pong');
    }

});

client.login('NzkyMTQ5MTY2ODU1Njg0MTE2.X-ZgZg.t3SA87xHjqHmKdyVG7kIHDN_e5k') 
