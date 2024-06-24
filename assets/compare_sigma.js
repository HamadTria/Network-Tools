function() {

    let start = Date.now();

    var container = document.getElementById('sigma-container-compare');

    while (container.firstChild) {
        container.removeChild(container.firstChild);
    }

    var s = new sigma({
        renderer: {
            container: container,
            type: 'webgl'
        },
    });

    var graphData = {
        nodes: [
            { id: "n0", label: "Node A", x: 0, y: 0, size: 3, color: '#75abd2' },
            { id: "n1", label: "Node B", x: 3, y: 1, size: 3, color: '#75abd2' },
            { id: "n2", label: "Node C", x: 1, y: 3, size: 3, color: '#75abd2' },
            { id: "n3", label: "Node D", x: 4, y: 2, size: 3, color: '#75abd2' },
            { id: "n4", label: "Node E", x: 2, y: 4, size: 3, color: '#75abd2' },
            { id: "n5", label: "Node F", x: 3, y: 3, size: 3, color: '#75abd2' },
            { id: "n6", label: "Node G", x: 0, y: 5, size: 3, color: '#75abd2' },
            { id: "n7", label: "Node H", x: 4, y: 4, size: 3, color: '#75abd2' },
            { id: "n8", label: "Node I", x: 5, y: 1, size: 3, color: '#75abd2' }
        ],
        edges: [
            { id: "e0", source: "n0", target: "n1", color: '#75abd2', type: 'line', size: 2 },
            { id: "e1", source: "n1", target: "n2", color: '#75abd2', type: 'curve', size: 2 },
            { id: "e2", source: "n2", target: "n0", color: '#75abd2', type: 'line', size: 2 },
            { id: "e3", source: "n1", target: "n3", color: '#75abd2', type: 'line', size: 2 },
            { id: "e4", source: "n3", target: "n4", color: '#75abd2', type: 'curve', size: 2 },
            { id: "e5", source: "n4", target: "n5", color: '#75abd2', type: 'line', size: 2 },
            { id: "e6", source: "n5", target: "n6", color: '#75abd2', type: 'curve', size: 2 },
            { id: "e7", source: "n6", target: "n7", color: '#75abd2', type: 'line', size: 2 },
            { id: "e8", source: "n7", target: "n8", color: '#75abd2', type: 'curve', size: 2 },
            { id: "e9", source: "n8", target: "n0", color: '#75abd2', type: 'line', size: 2 }
        ]
    };

    s.graph.read(graphData);

    s.refresh();

    let timeTaken = Date.now() - start;

    // Print the time taken to render the graph
    let timeText = document.createElement("p");
    timeText.innerText = "Time taken: " + timeTaken + "ms";
    timeText.style.position = "absolute";
    timeText.style.bottom = "10px";
    timeText.style.left = "10px";
    timeText.style.color = "#FFFFFF";
    timeText.style.fontSize = "0.8rem";
    container.appendChild(timeText);
}