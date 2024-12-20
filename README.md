# Genesis Demo Setup Project

This project documents the setup process and findings for running [Genesis](https://github.com/Genesis-Embodied-AI/Genesis), a universal and generative physics engine for robotics and embodied AI learning, on macOS with Apple Silicon.

## Quick Start

1. Clone this repository:
```bash
git clone https://github.com/yourusername/demo_setup_project.git
cd demo_setup_project
```

2. Clone required dependencies:
```bash
# Clone Genesis
git clone --recursive https://github.com/Genesis-Embodied-AI/Genesis.git

# Clone PyMeshLab
git clone --recursive https://github.com/cnr-isti-vclab/PyMeshLab.git
```

3. Set up Python environment:
```bash
# Create and activate virtual environment
python3.9 -m venv .venv
source .venv/bin/activate

# Install PyTorch
pip install torch --index-url https://download.pytorch.org/whl/cpu

# Install other dependencies
uv pip install scikit-image moderngl moderngl-window
```

4. Build PyMeshLab:
```bash
# Install build dependencies
brew install cmake ninja qt@5 coreutils libomp cgal xerces-c tbb embree

# Set up environment variables
export LDFLAGS="-L/opt/homebrew/opt/libomp/lib -L/opt/homebrew/opt/qt@5/lib"
export CPPFLAGS="-I/opt/homebrew/opt/libomp/include -I/opt/homebrew/opt/qt@5/include"
export PATH="/opt/homebrew/opt/qt@5/bin:$PATH"

# Build PyMeshLab
cd PyMeshLab
sh scripts/macos/1_build.sh
sh scripts/macos/2_deploy.sh
cd ..
```

5. Install Genesis:
```bash
# Install in development mode
PYTHONPATH=/path/to/project/Genesis pip install -e Genesis/
```

## Project Structure

```
demo_setup_project/
├── .venv/                 # Python virtual environment (created during setup)
├── Genesis/              # Genesis source code (cloned during setup)
├── PyMeshLab/            # PyMeshLab source code (cloned during setup)
├── test_genesis_*.py     # Various test scripts
└── README.md             # This file
```

## Test Scripts

The project includes several test scripts:

1. Basic simulation without visualization:
```bash
python test_genesis_simple.py
```

2. OpenGL visualization attempt:
```bash
python test_genesis_vis.py
```

3. Metal backend visualization attempt:
```bash
python test_genesis_metal.py
```

4. Raytracer visualization attempt:
```bash
python test_genesis_raytracer.py
```

## Current Status

### What Works
1. Basic Genesis installation and initialization
2. Physics simulation without visualization
3. Robot state querying and manipulation

### Known Issues

1. **OpenGL Visualization Issues**
   - Missing shader uniforms on macOS/Apple Silicon
   - Error messages:
     ```
     uniform not found: material.base_color_factor
     uniform not found: material.metallic_factor
     uniform not found: material.roughness_factor
     uniform not found: material.emissive_factor
     ```

2. **Metal Backend Issues**
   - Metal backend is recognized but not fully functional
   - Renderer configuration options are not exposed in the public API

3. **PyMeshLab Integration**
   - No pre-built wheels for Apple Silicon
   - Building from source is complex and has dependency issues

## Next Steps

### Potential Solutions to Explore

1. **Alternative Visualization Approaches**
   - Headless mode with frame saving
   - Alternative visualization libraries (MeshCat, PyViz3D)
   - Web-based viewer

2. **Custom Renderer Backend**
   - Build with Metal support
   - Implement software renderer
   - Use alternative rendering pipeline

3. **Different Visualization Strategy**
   - Run simulation headless and plot results
   - Use different robotics simulator with better macOS support

### Required Investigation

1. Research Metal backend implementation in Genesis
2. Investigate PyMeshLab alternatives or build fixes
3. Explore web-based visualization options

## Environment Details

```yaml
OS: macOS (Apple Silicon)
Python: 3.9
Key Dependencies:
  - genesis-world: 0.2.0
  - taichi: 1.7.2
  - PyOpenGL
  - moderngl
  - scikit-image
```

## Contributing

When continuing this work:
1. Check Genesis releases for Apple Silicon support
2. Look for PyMeshLab pre-built wheels for Apple Silicon
3. Consider containerization for consistent environment

## References

1. [Genesis Repository](https://github.com/Genesis-Embodied-AI/Genesis)
2. [PyMeshLab Repository](https://github.com/cnr-isti-vclab/PyMeshLab)
3. [Genesis Documentation](https://genesis-world.readthedocs.io/)

