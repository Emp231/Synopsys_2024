"""
from qgis.core import QgsPointXY, QgsFeature, QgsVectorLayer, QgsField, QgsProject, QgsPolygon, QgsGeometry

# Create a polygon memory layer
polygon_layer = QgsVectorLayer("Polygon?crs=EPSG:4326", "Polygon Layer", "memory")
provider = polygon_layer.dataProvider()

# Add attribute fields (optional)
field1 = QgsField("Name", QVariant.String)
field2 = QgsField("Value", QVariant.Double)
provider.addAttributes([field1, field2])
polygon_layer.updateFields()

# Define specific polygon coordinates (clockwise order)
polygon_coordinates = [
    QgsPointXY(-100.0, 40.0),
    QgsPointXY(-76.0, 41.0),
    QgsPointXY(-77.0, 42.0),
    QgsPointXY(-100.0, 40.0)  # Closing the polygon by repeating the first point
]

# Create a polygon geometry
polygon_geometry = QgsGeometry.fromPolygonXY([polygon_coordinates])

# Add the polygon to the layer
feature = QgsFeature()
feature.setGeometry(polygon_geometry)
feature.setAttributes(["Polygon A", 10.0])  # Replace with your attribute values
provider.addFeature(feature)

# Update layer extent
polygon_layer.updateExtents()

# Add the polygon layer to the project
QgsProject.instance().addMapLayer(polygon_layer)

print("Temporary polygon layer created and added to the project.")
"""