# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

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
CMAKE_SOURCE_DIR = /home/lapras/smart-fridge/code

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/lapras/smart-fridge/code

# Include any dependencies generated for this target.
include CMakeFiles/cpp-headless.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/cpp-headless.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/cpp-headless.dir/flags.make

CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o: CMakeFiles/cpp-headless.dir/flags.make
CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o: cpp-headless.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lapras/smart-fridge/code/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o -c /home/lapras/smart-fridge/code/cpp-headless.cpp

CMakeFiles/cpp-headless.dir/cpp-headless.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/cpp-headless.dir/cpp-headless.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lapras/smart-fridge/code/cpp-headless.cpp > CMakeFiles/cpp-headless.dir/cpp-headless.cpp.i

CMakeFiles/cpp-headless.dir/cpp-headless.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/cpp-headless.dir/cpp-headless.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lapras/smart-fridge/code/cpp-headless.cpp -o CMakeFiles/cpp-headless.dir/cpp-headless.cpp.s

CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o.requires:

.PHONY : CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o.requires

CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o.provides: CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o.requires
	$(MAKE) -f CMakeFiles/cpp-headless.dir/build.make CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o.provides.build
.PHONY : CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o.provides

CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o.provides.build: CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o


# Object files for target cpp-headless
cpp__headless_OBJECTS = \
"CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o"

# External object files for target cpp-headless
cpp__headless_EXTERNAL_OBJECTS =

cpp-headless: CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o
cpp-headless: CMakeFiles/cpp-headless.dir/build.make
cpp-headless: CMakeFiles/cpp-headless.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lapras/smart-fridge/code/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable cpp-headless"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/cpp-headless.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/cpp-headless.dir/build: cpp-headless

.PHONY : CMakeFiles/cpp-headless.dir/build

CMakeFiles/cpp-headless.dir/requires: CMakeFiles/cpp-headless.dir/cpp-headless.cpp.o.requires

.PHONY : CMakeFiles/cpp-headless.dir/requires

CMakeFiles/cpp-headless.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/cpp-headless.dir/cmake_clean.cmake
.PHONY : CMakeFiles/cpp-headless.dir/clean

CMakeFiles/cpp-headless.dir/depend:
	cd /home/lapras/smart-fridge/code && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lapras/smart-fridge/code /home/lapras/smart-fridge/code /home/lapras/smart-fridge/code /home/lapras/smart-fridge/code /home/lapras/smart-fridge/code/CMakeFiles/cpp-headless.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/cpp-headless.dir/depend

