function initializeCytoscape() {
    setTimeout(function() {

        let start = Date.now();

        var _nodes = JSON.parse(document.getElementById('bigdata-nodes').textContent);
        var _edges = JSON.parse(document.getElementById('bigdata-edges').textContent);

        var cyBigdata = window.cyBigdata = cytoscape({
            container: document.getElementById('bigdata-container'),
            ready: function(){},
            style: [
                {
                    selector: 'node',
                    css: {
                        'background-color': 'lightblue',
                        'color': '#fff',
                        'shape': 'ellipse',
                        'width': 10,
                        'height': 10,
                    }
                },
                {
                    selector: 'node:selected',
                    css: {
                        'border-color': 'red',
                        'border-width': 2,
                    }
                },
                {
                    selector: 'edge',
                    css: {
                        'target-arrow-shape': 'triangle',
                        'arrow-scale': 0.2,
                        'line-color': 'lightgray',
                        'target-arrow-color': 'lightgray',
                        'width': 0.3,
                    }
                },
                {
                    selector: '.mdi-contacts',
                    css: {
                        'background-color': 'lightseagreen',
                    }
                },
                {
                    selector: '.fas-message',
                    css: {
                        'background-color': 'lightblue',
                    }
                },
                {
                    selector: '.fas-person',
                    css: {
                        'background-color': 'lightgray',
                    }
                },
                {
                    selector: '.fas-phone',
                    css: {
                        'background-color': 'lightcoral',
                    }
                },
                {
                    selector: '.fas-sim-card',
                    css: {
                        'background-color': 'orange',
                    }
                },
                {
                    selector: '.fab-facebook',
                    css: {
                        'background-color': 'blue',
                    }
                },
                {
                    selector: '.fab-google',
                    css: {
                        'background-color': 'red',
                    }
                },
                {
                    selector: '.fab-instagram',
                    css: {
                        'background-color': 'purple',
                    }
                },
                {
                    selector: '.fab-telegram',
                    css: {
                        'background-color': 'lightgreen',
                    }
                },
                {
                    selector: '.fab-viber',
                    css: {
                        'background-color': 'pink',
                    }
                },
                {
                    selector: '.fab-whatsapp',
                    css: {
                        'background-color': 'green',
                    }
                },
            ],
            elements: {
                nodes: _nodes,
                edges: _edges
            },
            layout: {
                name: "random",
            },
        });

        let timeTaken = Date.now() - start;

        // Print the time taken to render the graph
        let timeText = document.createElement("p");
        timeText.innerText = "Time taken: " + timeTaken + "ms";
        timeText.style.position = "absolute";
        timeText.style.bottom = "10px";
        timeText.style.left = "10px";
        timeText.style.color = "#FFFFFF";
        timeText.style.fontSize = "0.8rem";
        document.getElementById('bigdata-container').appendChild(timeText);

        // Store original colors 
        cyBigdata.nodes().forEach(node => {
            node.data('originalColor', node.style('background-color'));
        });

        const contextMenuCommands = [
            {
                content: 'change size',
                select: function(ele){
                    if (ele.style('width') === '100' || ele.style('width') === '100px'){
                        cyBigdata.getElementById(ele.id()).animate({
                            style: { 'width': '30', 'height': '30' }
                        }, { duration: 500 });
                    } else {
                        cyBigdata.getElementById(ele.id()).animate({
                            style: { 'width': '100', 'height': '100' }
                        }, { duration: 500 });
                    }
                }
            },
            {
                content: 'isolate node',
                select: function(ele){
                    let connectedNodesAndEdges = ele.connectedEdges().connectedNodes().union(ele.connectedEdges()).union(ele);
                    if (cyBigdata.elements().not(connectedNodesAndEdges).style('visibility') === 'hidden'){
                        cyBigdata.elements().not(connectedNodesAndEdges).show();
                        cyBigdata.elements().not(connectedNodesAndEdges).style('visibility', 'visible');
                    } else {
                        cyBigdata.elements().not(connectedNodesAndEdges).hide();
                        cyBigdata.elements().not(connectedNodesAndEdges).style('visibility', 'hidden');
                    }
                }
            },
            {
                content: 'change shape',
                select: function(ele){
                    if (ele.style('shape') === 'square') {
                        cyBigdata.getElementById(ele.id()).style('shape', 'ellipse');
                    } else {
                        cyBigdata.getElementById(ele.id()).style('shape', 'square');
                    }
                }
            },
            {
                content: 'mark node',
                select: function(ele){
                    if (ele.style('background-color') === 'rgb(255,0,0)') {
                        cyBigdata.getElementById(ele.id()).style('background-color', ele.data('originalColor'));
                    } else {
                        cyBigdata.getElementById(ele.id()).style('background-color', 'red');
                    }
                }
            },
            {
                content: 'delete',
                select: function(ele){
                    cyBigdata.getElementById(ele.id()).hide();
                    cyBigdata.getElementById(ele.id()).style('visibility', 'hidden');
                }
            }
        ];

        // Apply context menu to graph
        cyBigdata.cxtmenu({
            selector: 'node',
            commands: contextMenuCommands
        });

        // Core context menu
        const coreContextMenuCommands = [
            {
                content: 'bring back nodes',
                select: function(){
                    cyBigdata.nodes().show();
                    cyBigdata.edges().show();
                    cyBigdata.edges().style('visibility', 'visible');
                    cyBigdata.nodes().style('visibility', 'visible');
                }
            },
            {
                content: 'reset colors',
                select: function(){
                    cyBigdata.nodes().forEach(node => {
                        node.style('background-color', node.data('originalColor'));
                    });
                }
            }
        ];

        // Apply core context menu to graph
        cyBigdata.cxtmenu({
            selector: 'core',
            commands: coreContextMenuCommands
        });

        cyBigdata.elements().qtip({
            content: function(){ return 'ID: ' + this.id() },
            position: {
                my: 'top center',
                at: 'bottom center'
            },
            style: {
                classes: 'qtip-bootstrap',
            }
        });

    }, 2000);
}
