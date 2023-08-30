import tensorflow as tf
import tensorflow_graphics.io as tfg
import tensorflow_graphics.geometry.representation.point as tfg_point
import tensorflow_graphics.io.triangle_mesh as tfg_mesh
import tensorflow_graphics.geometry.representation.mesh.sampler as tfg_mesh_sampler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow_graphics.geometry as tfg_geo
import trimesh 
import numpy as np  

def convert_stl_to_point_cloud(stl_filename, num_samples):
    print("Loading STL file as a mesh...")
    stl_mesh = tfg.triangle_mesh.load(stl_filename)
    
    print("Sampling points from the mesh...")
    sampled_points = tfg_point.sample_uniformly(stl_mesh.vertices, num_samples)
    
    print("Converting sampled points to a point cloud tensor...")
    point_cloud = tf.convert_to_tensor(sampled_points, dtype=tf.float32)
    
    return point_cloud

def convert_stl_to_point_cloud_2(stl_filename, num_samples):
    print("Loading STL file as a mesh...")
    stl_mesh = trimesh.load(stl_filename, file_type="stl")

    
    print("Sampling points from the mesh using weighted random sampling...")
    sampled_points = tfg_mesh_sampler.weighted_random_sample_triangle_mesh(stl_mesh, num_samples)
    
    print("Converting sampled points to a point cloud tensor...")
    point_cloud = tf.convert_to_tensor(sampled_points, dtype=tf.float32)
    
    return point_cloud

def convert_stl_to_point_cloud_3(stl_filename):
    print("Loading STL file as a mesh...")
    stl_mesh = tfg.triangle_mesh.load(stl_filename)
    
    print("Converting mesh to a point cloud using tfg_point.from_mesh...")
    point_cloud = tfg_point.from_mesh(stl_mesh, dtype=tf.float32)
    
    return point_cloud


def convert_mesh_to_one_dimensional(mesh):
    # Flatten the vertices of the mesh into a single list of numbers
    flattened_vertices = mesh.vertices.ravel()
    return flattened_vertices

def convert_stl_to_point_cloud_4(stl_filename, num_samples):
    # Load the STL file as a mesh
    stl_mesh = trimesh.load(stl_filename)
    one_dim_representation = convert_mesh_to_one_dimensional(stl_mesh)
    # Sample points from the mesh's vertices
    sampled_points = np.random.choice(one_dim_representation, size=num_samples, replace=False)
    
    # Convert the sampled points to a point cloud tensor
    point_cloud = tf.convert_to_tensor(sampled_points, dtype=tf.float32)
    
    return point_cloud

def visualize_point_cloud(point_cloud):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = point_cloud[:, 0]
    y = point_cloud[:, 1]
    z = point_cloud[:, 2]
    
    ax.scatter(x, y, z, marker='.')
    
    plt.show()

def main():
    stl_filename = "/home/cherryhead/Desktop/burn/webscraping/python-scripts/stl/3DBenchy.stl"
    num_samples = 1000
    print("Start converting STL file to point cloud...")
    point_cloud = convert_stl_to_point_cloud_4(stl_filename, num_samples)
    visualize_point_cloud(point_cloud)

if __name__ == "__main__":
    main()
