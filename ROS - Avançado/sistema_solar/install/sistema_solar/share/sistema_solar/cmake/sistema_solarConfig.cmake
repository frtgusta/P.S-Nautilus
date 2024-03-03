# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_sistema_solar_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED sistema_solar_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(sistema_solar_FOUND FALSE)
  elseif(NOT sistema_solar_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(sistema_solar_FOUND FALSE)
  endif()
  return()
endif()
set(_sistema_solar_CONFIG_INCLUDED TRUE)

# output package information
if(NOT sistema_solar_FIND_QUIETLY)
  message(STATUS "Found sistema_solar: 0.0.0 (${sistema_solar_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'sistema_solar' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${sistema_solar_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(sistema_solar_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${sistema_solar_DIR}/${_extra}")
endforeach()
