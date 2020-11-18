var path = require('path');

module.exports = function(RED) {
    function GroveTimeOfFlightDistance(config) {
        RED.nodes.createNode(this,config);

        this.port_name = "I2C";
        this.status({fill:"blue", shape:"dot", text:this.port_name});

        var node = this;

        const spawn = require('child_process').spawn;
        const grove_python = spawn('python', [ '-u' , path.join( __dirname , 'grove-time-of-flight-distance.py' ) ]);
        this.status({fill:"green",shape:"dot",text:this.port_name + " listened"});

        grove_python.stdout.on('data', (data) => {
            node.log(`Distance = ${data} mm`);

            this.status({ fill: "blue", shape: "dot", text: this.port_name + " value chanded" });
            let _self = this;

            msg = {};
            
            msg.payload = parseInt(data);
            node.send(msg);
            
            setTimeout(
                function(){
                    _self.status({fill:"green",shape:"dot",text:_self.port_name + " listened"});
                },200
            )
            
        });
        
        grove_python.stderr.on('data', (data) => {
            this.status({fill:"red",shape:"ring",text:this.port_name + " error"});

            let jsonData = parseInt(data);
            msg = {};
            msg.payload = jsonData;
            node.send(msg);
        });
        
        grove_python.on('close', (code) => {
            this.status({fill:"red",shape:"ring",text:this.port_name + " disconnected"});

            let jsonData = "child process exited with code " + code;
            msg = {};
            msg.payload = jsonData;
            node.send(msg);
        });
    }
    
    RED.nodes.registerType("grove-time-of-flight-distance", GroveTimeOfFlightDistance);
}
