cmake_minimum_required(VERSION 3.0...3.28)
file(STRINGS "SDK_VERSION" SDK_VERSION)
project(inno_clientsdk
        VERSION ${SDK_VERSION})

set(INNO_SDK_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
set(INNO_SDK_VERSION_MINOR ${PROJECT_VERSION_MINOR})
set(INNO_SDK_VERSION_PATCH ${PROJECT_VERSION_PATCH})
set(INNO_SDK_VERSION_TWEAK ${PROJECT_VERSION_TWEAK})
add_subdirectory(src)

option(MAKE_SHARED "Build a shared library" OFF)

if(NOT MAKE_SHARED)
    if(EXISTS "${CMAKE_SOURCE_DIR}/apps/example")
        add_subdirectory(apps/example)
    endif()

    if(EXISTS "${CMAKE_SOURCE_DIR}/apps/tools/get_pcd/")
        add_subdirectory(apps/tools/get_pcd)
    endif()
endif()

include(CMakePackageConfigHelpers)
configure_package_config_file(
        "inno-client-config.cmake.in" "inno-client-config.cmake"
        INSTALL_DESTINATION "${CMAKE_INSTALL_LIBBDIR}/cmake/inno-client-config"
)
write_basic_package_version_file(
        "inno-client-version.cmake"
        VERSION {INNO_SDK_VERSION_MAJOR}.${INNO_SDK_VERSION_MINOR}.${INNO_SDK_VERSION_PATCH}
        COMPATIBILITY ExactVersion
)

install(TARGETS inno_client_sdk
        EXPORT inno-client-sdk-targets
)

install( FILES
        ${CMAKE_CURRENT_BINARY_DIR}/inno-client-config.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/inno-client-version.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/inno-client-config
)

install(EXPORT inno-client-sdk-targets
        NAMESPACE inno_client_sdk::
        FILE inno-client-sdk-targets.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/inno-client-config
)
