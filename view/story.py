import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc

def  sigm_story():
    text = """
    Sigma.js is a powerful JavaScript library used for drawing network graphs in web applications. Here are some of the key advantages and disadvantages of using Sigma.js for plotting network graphs:

    ### Advantages

    1. **Performance**:
    - Sigma.js is designed to handle large networks efficiently. It leverages WebGL for rendering, which allows it to handle thousands of nodes and edges smoothly on modern browsers.

    2. **Interactivity**:
    - Sigma.js provides built-in interactivity features such as zooming, panning, node dragging, and event handling (e.g., clicking on nodes or edges). This makes it easy to create dynamic and interactive network visualizations.

    3. **Customizability**:
    - The library is highly customizable. You can change the appearance of nodes, edges, and labels using various settings and styles. It also supports custom rendering functions for more advanced visualizations.

    4. **Easy Integration**:
    - Sigma.js can be easily integrated into web applications. It works well with modern front-end frameworks like React, Angular, and Vue.js, making it suitable for a wide range of web development projects.

    5. **Open Source**:
    - As an open-source library, Sigma.js is free to use and has an active community. This means you can benefit from community support and contributions.

    ### Disadvantages

    1. **Learning Curve**:
    - While Sigma.js is powerful, it can be complex to learn and use effectively, especially for beginners who are not familiar with JavaScript or network visualization concepts.

    2. **Documentation**:
    - Although there is documentation available, some users find it lacking in depth and examples. This can make it challenging to implement advanced features or troubleshoot issues.

    3. **Limited Built-in Layouts**:
    - Sigma.js comes with basic layout algorithms, but for more advanced or specific layout needs, you may need to rely on external libraries or plugins. This can complicate the setup and integration process.

    4. **Integration Complexity**:
    - For very specific use cases or highly customized visualizations, integrating Sigma.js can become complex and may require substantial custom development work.

    Overall, Sigma.js is a robust choice for network visualization in web applications, offering a balance of performance, customizability, and interactivity. However, its complexity and the potential need for additional development effort should be considered when choosing it for a project.
    """

    return dbc.Card([
        dbc.CardBody([
            dcc.Markdown(text)
        ])
    ])

def cyto_story():
    text = """
    Cytoscape is a versatile tool for network graph visualization and analysis, available both as a desktop application and a JavaScript library (Cytoscape.js). Here are some of the key advantages and disadvantages of using Cytoscape for plotting network graphs:

    ### Advantages

    1. **Comprehensive Analysis Tools**:
    - Cytoscape provides a wide array of analysis tools and algorithms, including those for clustering, pathway analysis, and network statistics, making it suitable for complex biological and other types of data analysis.

    2. **Rich Visualization Features**:
    - It offers extensive visualization options, including a variety of node and edge styles, layouts, and the ability to create custom visualizations. The desktop version allows for sophisticated styling and detailed customization.

    3. **Extensibility and Plugins**:
    - Cytoscape has a large ecosystem of plugins (apps) that extend its functionality. These plugins cover a wide range of additional features, from specialized analysis methods to enhanced visualization techniques.

    4. **Active Community and Support**:
    - Cytoscape has a strong user community and active development, providing ample support, tutorials, and documentation. This community-driven support can be very beneficial for troubleshooting and learning.

    ### Disadvantages

    1. **Complexity and Learning Curve**:
    - Cytoscape, especially the desktop application, can be complex to learn due to its wide range of features and options. Users need time to become proficient in utilizing its full capabilities.

    2. **Performance Issues with Large Networks**:
    - Although Cytoscape is powerful, it may struggle with very large networks, especially in the desktop application. Performance can degrade with increasing network size and complexity.

    3. **Desktop vs. Web Application**:
    - While the desktop application is feature-rich, it requires installation and is not as easily shared as web-based visualizations. Cytoscape.js addresses this but may not have all the features of the desktop version.

    4. **Resource Intensive**:
    - The desktop application can be resource-intensive, requiring significant memory and processing power, especially for larger datasets and complex visualizations.

    Overall, Cytoscape is a powerful and flexible tool for network visualization and analysis, particularly well-suited for biological research. Its extensive features and active community make it a strong choice, though its complexity and potential performance limitations should be considered based on the specific use case.
    """

    return dbc.Card([
        dbc.CardBody([
            dcc.Markdown(text)
        ])
    ])