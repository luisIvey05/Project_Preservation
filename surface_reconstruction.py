import open3d as o3d
import numpy as np
from PIL import Image
import glob
from open3d_example import draw_geometries_flip

# mesh = o3d.io.read_triangle_mesh("./fragment_013.ply")
# print(mesh)
# mesh.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh])
# pcd = mesh.sample_points_uniformly(number_of_points=500)
# o3d.visualization.draw_geometries([pcd])

fragment_files = glob.glob("fragments/*.ply")

for i in range(0, len(fragment_files)):
    print(fragment_files[i])
    pcd = o3d.io.read_point_cloud(fragment_files[i])
    draw_geometries_flip([pcd])

# fragment_file = "fragment_013.ply"
# pcd = o3d.io.read_point_cloud(fragment_file)
# draw_geometries_flip([pcd])