var path = require('path');

module.exports = function(RED) {
    function GroveOLEDDisplay128x64(config) {
        RED.nodes.createNode(this,config);

        this.port_name = "I2C";
        this.status({fill:"blue",shape:"dot",text:this.port_name});
        
        var node = this;
        node.on('input', function(msg) {
            // msg.payload = msg.payload.toLowerCase();
            const exec = require('child_process').exec;
            // const message = msg.payload.message;
            const message = msg.payload;  // Changed simple string payload in v.0.0.4.
            //console.log(clear);
            this.status({fill:"yellow",shape:"ring",text:this.port_name + " connecting"});
            exec('python -u ' + path.join( __dirname , 'grove-oled-display-128x64.py') + ' "' + message + '"', (err, stdout, stderr) => {
                if (err) { console.log(err); }
                // console.log(stdout);
                this.status({fill:"green",shape:"dot",text:this.port_name + " connected"});
            });
            
            // node.send(msg);
        });
    }
    RED.nodes.registerType("grove-oled-display-128x64",GroveOLEDDisplay128x64);
}
