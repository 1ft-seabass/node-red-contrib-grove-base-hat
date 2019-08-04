var path = require('path');

module.exports = function(RED) {
    function GroveLightSensorV1_2Node(config) {
        RED.nodes.createNode(this,config);

        this.port_number = config.port_number;

        this.port_name = "A" + this.port_number;
        this.status({fill:"blue",shape:"dot",text:this.port_name});

        var node = this;
        node.on('input', function(msg) {

            const gpio_pin = this.port_number;

            const exec = require('child_process').exec;
            this.status({fill:"yellow",shape:"ring",text:this.port_name + " connecting"});
            exec('python -u ' + path.join( __dirname , 'grove-light-sensor-v1_2.py' ) + ' ' + gpio_pin + ' ' + msg.payload, (err, stdout, stderr) => {
                if (err) { console.log(err); }
                let str = stdout.toString();
                let jsonData;
                try {
                    jsonData = JSON.parse(str);
                } catch (e) {
                    jsonData = e.toString();
                }
                msg.payload = jsonData;
                this.status({fill:"green",shape:"dot",text:this.port_name + " connected"});
                node.send(msg);
            });
        });
    }
    RED.nodes.registerType("grove-light-sensor-v1_2",GroveLightSensorV1_2Node);
}
