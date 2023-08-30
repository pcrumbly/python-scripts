import tensorflow as tf
import tensorflow_graphics.geometry.representation.point as tfg_point
import tensorflow_graphics.io as tfg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow_graphics.geometry as tfg_geo

def convert_stl_to_point_cloud(stl_filename, num_samples):
    # Load the STL file as a mesh
    stl_mesh = tfg.triangle_mesh.load(stl_filename)
    
    # Sample points from the mesh
    sampled_points = tfg_point.sample_uniformly(stl_mesh.vertices, num_samples)
    
    # Convert the sampled points to a point cloud tensor
    point_cloud = tf.convert_to_tensor(sampled_points, dtype=tf.float32)
    
    return point_cloud

def convert_stl_to_point_cloud_2(stl_filename, num_samples):
    # Load the STL file as a mesh
    stl_mesh = tfg.triangle_mesh.load(stl_filename)
    
    # Sample points from the mesh
    sampled_points = tfg_geo.representation.mesh.sampler.weighted_random_sample_triangle_mesh(stl_mesh.vertices, num_samples)
    
    # Convert the sampled points to a point cloud tensor
    point_cloud = tf.convert_to_tensor(sampled_points, dtype=tf.float32)
    
    return point_cloud

def convert_stl_to_point_cloud_3(stl_filename):
    # Load the STL file as a mesh
    stl_mesh = tfg.triangle_mesh.load(stl_filename)
    
    # TODO Convert the mesh to a point cloud
    # Need to sample the mesh for points and convert to a point cloud
    # Specify the number of samples and the point type
    point_cloud = tfg_point.from_mesh(stl_mesh, dtype=tf.float32)
    
    return point_cloud

def visualize_point_cloud(point_cloud):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Extract x, y, z coordinates from the point cloud tensor
    x = point_cloud[:, 0]
    y = point_cloud[:, 1]
    z = point_cloud[:, 2]
    
    # Create the scatter plot
    ax.scatter(x, y, z, marker='.')
    
    plt.show()

def main():
    stl_filename = "stl/3DBenchy.stl"
    
    # Convert STL to point cloud
    point_cloud = convert_stl_to_point_cloud_2(stl_filename)
    
    # Visualize the point cloud
    visualize_point_cloud(point_cloud)

if __name__ == "__main__":
    main()