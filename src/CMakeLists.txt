cmake_minimum_required( VERSION 3.0...3.28)
project(inno_client_sdk)  

add_library(inno_client_sdk)

target_include_directories(
		inno_client_sdk
		PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
		$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

set_target_properties(${PROJECT_NAME} PROPERTIES VERSION
${INNO_SDK_VERSION_MAJOR}.${INNO_SDK_VERSION_MINOR}.${INNO_SDK_VERSION_PATCH} SOVERSION ${INNO_SDK_VERSION_MAJOR})

if (CMAKE_SYSTEM_NAME STREQUAL "Linux")
	target_link_libraries(inno_client_sdk PRIVATE pthread)
endif ()
if (CMAKE_SYSTEM_NAME STREQUAL "Darwin")
	target_link_libraries(inno_client_sdk PRIVATE pthread)
endif ()

add_subdirectory (utils)
add_subdirectory (sdk_common)
add_subdirectory (sdk_client)

