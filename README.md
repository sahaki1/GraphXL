# Graph XL

This application loads data from an Excel file to generate a diagram/graph that represents relatinships between each row in an Excel worksheet.

[ Video Demo ](#video-demo)\
[ Graph XL Design ](#graph-xl-design)\
[ User Guide ](#user-guide)\
[ Author ](#author)\
[ License ](#license)

## Video Demo  
[![Graph XL Video](![image](https://user-images.githubusercontent.com/48220157/140672293-80d47233-2c84-48c7-a92a-bd8e4137d620.png))](https://youtu.be/9j0ZJu2rmgg)

## Graph XL Design
Although Graph XL is mainly a Javascript application it is launched as a Flask app.\
`flask run app.py`\
Where `app.py` is fount in the root project folder. The remaider of the code files have been grouped as part of a flask package
called `graphxl`. The 1graphxl` package contains the following key folders and files.\
- **external**, 
	- `bootstrap`, is a folder that contains the bootstrap CSS and JS files referenced by the application.
	- `mxgraph`, is a folder that contains the mxgraph 2D graph library that allows for the rendering of the diagrams.
	- `sheetJs`, is a folder that contains the `xlsx.js` file that is used by the application to load/open Excel files and tranform the data to JSON.
- **libraries**,
	- `graphxl.js`, is a file containing the functions needed for I/O, HTML interactions and functions to manipulate the graph.
	- `grpahxlData.js`, is a global data cache/object that is loaded with common data such as the Excel worksheet name.
	- `graphxlEvents.js`, is a file containing event handling functions for the application.
	- `menubar.css`, is a CSS file containing the style for the menubar/navbar of the application 
	and supports large and small (mobile device) form factors.
	- `menubar.js`, is a file containing the functions that define the behaviour of any navbar that uses the menubar.css styles.
- **resources**,
- **templates**,
	- `about.html`, is an HTML page contining info about the applications and instructions on how to use it.
	- `base.html`, is the base template inherited by all other HTML file and contains JINJA placeholders.
	All JS/CSS required by all other HTML files are also loaded here. 
	All common HTML page element are also defined in this template.
	This file also load the saved data from the local storage into the graphData object.
	- `base_controls.html`, contains all HTML + JS code that define the controls used by the application.
	- `data.html`, injects the `homeDataTable` into the tamplate page that will display the columns and rows loaded from Excel.
	- `graph.html`, injects the `graphContainer` into the tamplate page which is what mxGraph uses to display the graph.

### Design Decisions
Id  | Decision
----| -------------
1  | I decided to package my code as a Flask package to gain the experience and make it more reusable in future projects.
2  | I decided to repoint the `static_url_path` and `static_folder` to the root of the graphxl package folder in order to accomodate my package folder structure.
3  | 

## User Guide
To use this application you will first need to run the Flask application (app.py).
1. Launch the application and follow these steps to generate a diagram.
2. Load an Excel file by selecting the 'File->Open' menu item.
3. If the Excel file is successfully loaded, the diagram should have been auto-generated.
	- If the diagram is not generated, use the menu item 'Graph->Generate Graph'.
5. To see the data behind the graph you can open the graph properties dialog ('View->Graph Properties' menu item) and select a vertex to see the properties of that vertex.
	- Or, you can view table of all the data via 'view->Data' menu item

### Excel Template
When loading data from an Excel workbook the default worksheet name that the application looks for is 'Data'. However you can change the default name of the worksheet that the application is expecting using the File->settings dialog.

There are some mandatory fields that need to be included in the Excel data sheet.
- **Id:** unique ID of a given row.
- **Name:** name/title that represents the item.
- **Rel_[ID]:** represents an association between this given row and another row. The value here is the ID of the other row. You may have up to 10 of these fiels with a unique value for [ID].
- **Rel_[ID]_Label:** is the associated label for the given Rel_[ID] association. The value in this field will be displayed as the value for the connector/edge label.
- **Fill:** the fill color that will be used for the node/vertex that will represent the row.
- **Stroke:** the line color that will be used for the node/vertex that will represent the row.
- **Image:** the uri to the image that will be used for the node/vertex that will represent the row.

You may add additional fields beyond these to your Excel sheet. See a sample Excel file in the '/data' directory of the project.

### Author
Issam Sahak\
[@sahaki](https://github.com/sahaki1)

### License
[MIT](https://choosealicense.com/licenses/mit/)
