# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/davidlin/catkin_ws_toyboys/src/fub_remap_joystick

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/davidlin/catkin_ws_toyboys/build/fub_remap_joystick

# Include any dependencies generated for this target.
include CMakeFiles/fub_remap_joystick.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/fub_remap_joystick.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/fub_remap_joystick.dir/flags.make

CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o: CMakeFiles/fub_remap_joystick.dir/flags.make
CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o: /home/davidlin/catkin_ws_toyboys/src/fub_remap_joystick/src/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/davidlin/catkin_ws_toyboys/build/fub_remap_joystick/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o -c /home/davidlin/catkin_ws_toyboys/src/fub_remap_joystick/src/main.cpp

CMakeFiles/fub_remap_joystick.dir/src/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fub_remap_joystick.dir/src/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/davidlin/catkin_ws_toyboys/src/fub_remap_joystick/src/main.cpp > CMakeFiles/fub_remap_joystick.dir/src/main.cpp.i

CMakeFiles/fub_remap_joystick.dir/src/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fub_remap_joystick.dir/src/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/davidlin/catkin_ws_toyboys/src/fub_remap_joystick/src/main.cpp -o CMakeFiles/fub_remap_joystick.dir/src/main.cpp.s

CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o.requires:

.PHONY : CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o.requires

CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o.provides: CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/fub_remap_joystick.dir/build.make CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o.provides.build
.PHONY : CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o.provides

CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o.provides.build: CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o


# Object files for target fub_remap_joystick
fub_remap_joystick_OBJECTS = \
"CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o"

# External object files for target fub_remap_joystick
fub_remap_joystick_EXTERNAL_OBJECTS =

/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: CMakeFiles/fub_remap_joystick.dir/build.make
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libnodeletlib.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libbondcpp.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libclass_loader.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/libPocoFoundation.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libdl.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libroslib.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/librospack.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libpython2.7.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_program_options.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libtinyxml2.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libroscpp.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/librosconsole.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/librosconsole_log4cxx.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/librosconsole_backend_interface.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libxmlrpcpp.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libroscpp_serialization.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/librostime.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libcpp_common.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/libfub_remap_joystick_nodelet.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libnodeletlib.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libbondcpp.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libclass_loader.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/libPocoFoundation.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libdl.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libroslib.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/librospack.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libpython2.7.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_program_options.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libtinyxml2.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libroscpp.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/librosconsole.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/librosconsole_log4cxx.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/librosconsole_backend_interface.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libxmlrpcpp.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libroscpp_serialization.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/librostime.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /opt/ros/melodic/lib/libcpp_common.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick: CMakeFiles/fub_remap_joystick.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/davidlin/catkin_ws_toyboys/build/fub_remap_joystick/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/fub_remap_joystick.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/fub_remap_joystick.dir/build: /home/davidlin/catkin_ws_toyboys/devel/.private/fub_remap_joystick/lib/fub_remap_joystick/fub_remap_joystick

.PHONY : CMakeFiles/fub_remap_joystick.dir/build

CMakeFiles/fub_remap_joystick.dir/requires: CMakeFiles/fub_remap_joystick.dir/src/main.cpp.o.requires

.PHONY : CMakeFiles/fub_remap_joystick.dir/requires

CMakeFiles/fub_remap_joystick.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/fub_remap_joystick.dir/cmake_clean.cmake
.PHONY : CMakeFiles/fub_remap_joystick.dir/clean

CMakeFiles/fub_remap_joystick.dir/depend:
	cd /home/davidlin/catkin_ws_toyboys/build/fub_remap_joystick && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/davidlin/catkin_ws_toyboys/src/fub_remap_joystick /home/davidlin/catkin_ws_toyboys/src/fub_remap_joystick /home/davidlin/catkin_ws_toyboys/build/fub_remap_joystick /home/davidlin/catkin_ws_toyboys/build/fub_remap_joystick /home/davidlin/catkin_ws_toyboys/build/fub_remap_joystick/CMakeFiles/fub_remap_joystick.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/fub_remap_joystick.dir/depend

