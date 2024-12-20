import genesis as gs
import time
import sys

def main():
    try:
        # Initialize Genesis with Metal backend
        gs.init(backend=gs.metal)

        # Create a scene with visualization
        scene = gs.Scene(
            sim_options=gs.options.SimOptions(),
            viewer_options=gs.options.ViewerOptions(
                camera_pos=(3.5, 0.0, 2.5),
                camera_lookat=(0.0, 0.0, 0.5),
                camera_up=(0.0, 0.0, 1.0),
                camera_fov=40,
                res=(1280, 720),
                refresh_rate=60,
                max_FPS=60,
            ),
            show_viewer=True,
            rigid_options=gs.options.RigidOptions(
                dt=0.01,
                gravity=(0.0, 0.0, -10.0),
            ),
            renderer_type='metal',  # Use Metal renderer
        )

        # Add a plane and a Franka robot
        plane = scene.add_entity(gs.morphs.Plane())
        robot = scene.add_entity(
            gs.morphs.MJCF(file="Genesis/genesis/assets/xml/franka_emika_panda/panda.xml"),
        )

        # Build the scene
        print("Building scene...")
        scene.build()

        # Define simulation function
        def run_sim(scene, robot):
            print("\nStarting simulation...")
            t_prev = time.time()
            i = 0
            try:
                while True:
                    scene.step()
                    
                    # Print stats every second
                    t_now = time.time()
                    if t_now - t_prev >= 1.0:
                        print(f"\nStep {i}:")
                        print(f"FPS: {i / (t_now - t_prev):.1f}")
                        print("Robot joint positions:", robot.get_dofs_position())
                        t_prev = t_now
                        i = 0
                    i += 1
            except KeyboardInterrupt:
                print("\nSimulation stopped by user")

        # Run simulation in a separate thread
        print("Starting viewer...")
        gs.tools.run_in_another_thread(fn=run_sim, args=(scene, robot))
        
        # Start the viewer (this will block until the window is closed)
        scene.viewer.start()

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
