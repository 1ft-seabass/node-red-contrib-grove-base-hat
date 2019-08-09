var path = require('path');

module.exports = function(RED) {
    function GroveI2CColorSensorV2(config) {
        RED.nodes.createNode(this,config);
        
        this.port_name = "I2C";
        this.status({fill:"blue",shape:"dot",text:this.port_name});

        var node = this;
        node.on('input', function(msg) {
            const exec = require('child_process').exec;
            this.status({fill:"yellow",shape:"ring",text:this.port_name + " connecting"});
            exec('python -u ' + path.join( __dirname , 'grove-i2c-color-sensor-v2.py' ), (err, stdout, stderr) => {
                if (err) { console.log(err); }
                // console.log(stdout);
                msg.payload = JSON.parse(stdout);
                this.status({fill:"green",shape:"dot",text:this.port_name + " connected"});
                node.send(msg);
            });
        });
    }
    RED.nodes.registerType("grove-i2c-color-sensor-v2",GroveI2CColorSensorV2);
}
