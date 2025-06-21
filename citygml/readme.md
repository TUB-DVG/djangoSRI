## Info

This folder contains the CityGML model for the proposed ADE. The model is based on the [CityGML 2.0 standard](https://www.opengeospatial.org/standards/citygml). A mappping to 3.0 is currently not planned.



## Resources 

The UML model of the CityGML SRIADE was created with the help of the software [Enterprise Architect](https://sparxsystems.com/products/ea/). The UML folder provides the EAP file, which can be opened with Enterprise Architect, the UML diagramm as PDF. 

The XML Schema file of the UtilityNetwork ADE was automatically generated from the UML model with the help of the [ShapeChange](https://shapechange.net/). The XSD folder proivdes the generated XSD file and the code list dictionary You can also directly export the XSD from EA, via 'Generate GML Application schema'. 


ShapeChange requires a configuration file to derice the XML Schema. The ShapeChange folder contains the configuration file. 

The strucutre and concept is derived from [Tatjana Kutzner and the utility network ADE](https://github.com/TatjanaKutzner/CityGML-UtilityNetwork-ADE). Note, that the ShapeChange config has beend modified in version 4.0, you can see the adjusted names in the [documentation](https://github.com/ShapeChange/ShapeChange/wiki/Migration-to-ShapeChange-v4.0.0). 










