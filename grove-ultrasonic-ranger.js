module.exports = function(RED) {
    function GroveUltraSonicNode(config) {
        RED.nodes.createNode(this,config);

        this.port_number = config.port_number;

        this.port_name = "D" + this.port_number;
        this.status({fill:"blue",shape:"dot",text:this.port_name});

        var node = this;
        node.on('input', function(msg) {

            const gpio_pin = this.port_number;

            const exec = require('child_process').exec;
            this.status({fill:"yellow",shape:"ring",text:this.port_name + " connecting"});
            exec('python -u grove-ultrasonic-ranger.py ' + gpio_pin + ' ' + msg.payload, (err, stdout, stderr) => {
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
    RED.nodes.registerType("grove-ultrasonic-ranger",GroveUltraSonicNode);
}
