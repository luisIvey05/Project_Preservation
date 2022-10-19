import open3d as o3d


def get_3d_point_cloud(image_pth, depth):
    rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(o3d.io.read_image(image_pth), o3d.geometry.Image(depth),
                                                              convert_rgb_to_intensity=False)
    intrinsic = o3d.camera.PinholeCameraIntrinsic(width = 1242, height = 375, fx = 721., fy = 721., cx = 609., cy = 609.)

    point_cloud = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, intrinsic)
    o3d.io.write_point_cloud("KITTI.pcd", point_cloud)
    o3d.visualization.draw_geometries([point_cloud])