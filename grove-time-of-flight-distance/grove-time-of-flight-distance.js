var path = require('path');

module.exports = function(RED) {
    function GroveTimeOfFlightDistance(config) {
        RED.nodes.createNode(this,config);

        this.port_name = "I2C";
        this.status({fill:"blue", shape:"dot", text:this.port_name});

        var node = this;
        node.on('input', function(msg) {
            const exec = require('child_process').exec;
            this.status({fill:"yellow", shape:"ring", text:this.port_name + " connecting"});

            exec('python -u ' + path.join( __dirname , 'grove-time-of-flight-distance.py' ) + ' ' + msg.payload, (err, stdout, stderr) => {
                if (err) { console.log(err); }
                console.log('stdout', stdout);
                msg.payload = stdout;
                this.status({fill:"green",shape:"dot",text:this.port_name + " connected"});
                node.send(msg);
            });
        });
    }
    
    RED.nodes.registerType("grove-ultrasonic-ranger", GroveTimeOfFlightDistance);
}
