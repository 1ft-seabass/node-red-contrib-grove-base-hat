var path = require('path');

module.exports = function(RED) {
    function GroveLedNode(config) {
        RED.nodes.createNode(this,config);

        this.port_number = config.port_number;

        this.port_name = "D" + this.port_number;
        this.status({fill:"blue",shape:"dot",text:this.port_name});
        
        var node = this;
        node.on('input', function(msg) {
            // msg.payload = msg.payload.toLowerCase();
            const gpio_pin = this.port_number;
            const exec = require('child_process').exec;
            const message = msg.payload.message;
            let colon = 0;
            if( msg.payload.colon ){
                colon = msg.payload.colon;
            }
            //console.log(colon);
            let clear = 0;
            if( msg.payload.clear ){
                clear = msg.payload.clear;
            }
            //console.log(clear);
            this.status({fill:"yellow",shape:"ring",text:this.port_name + " connecting"});
            exec('python -u ' + path.join( __dirname , 'grove-4-digit-display.py') + ' ' + gpio_pin + ' ' + message + ' ' + colon + ' ' + clear, (err, stdout, stderr) => {
                if (err) { console.log(err); }
                // console.log(stdout);
                this.status({fill:"green",shape:"dot",text:this.port_name + " connected"});
            });
            
            // node.send(msg);
        });
    }
    RED.nodes.registerType("grove-4-digit-display",GroveLedNode);
}
