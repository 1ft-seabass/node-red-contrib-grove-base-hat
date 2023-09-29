var path = require('path');

module.exports = function(RED) {
    function GroveTemperatureHumiditySensorSHT3x(config) {
        RED.nodes.createNode(this,config);
        
        this.port_name = "I2C";
        this.status({fill:"blue",shape:"dot",text:this.port_name});

        var node = this;
        node.on('input', function(msg) {
            const exec = require('child_process').exec;
            this.status({fill:"yellow",shape:"ring",text:this.port_name + " connecting"});
            
            try {
                exec('python -u ' + path.join( __dirname , 'grove-temperature-humidity-sensor-sht3x.py' ) + ' ' + config.model, (err, stdout, stderr) => {
                    if (err) { console.log(err); }
                    console.log(stdout);
                    msg.payload = JSON.parse(stdout);
                    msg.payload.temperature = Number(msg.payload.temperature);
                    msg.payload.humidity = Number(msg.payload.humidity);
                    this.status({fill:"green",shape:"dot",text:this.port_name + " connected"});
                    node.send(msg);
                });
            } catch (e){
                console.error(e);
            }
            
        });
    }
    RED.nodes.registerType("grove-temperature-humidity-sensor-sht3x",GroveTemperatureHumiditySensorSHT3x);
}
