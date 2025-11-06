project(demo)
cmake_minimum_required(VERSION 3.0...4.0)

add_executable(demo ${PROJECT_SOURCE_DIR}/demo.cpp)
target_link_libraries(demo PRIVATE inno_client_sdk)

add_executable(sphere2xyz ${PROJECT_SOURCE_DIR}/sphere2xyz.cpp)
target_link_libraries(sphere2xyz PRIVATE inno_client_sdk)


########################
set(targets demo sphere2xyz)

foreach(target ${targets})
    INSTALL(TARGETS ${target}
        RUNTIME DESTINATION ${PROJECT_SOURCE_DIR}/
    )
endforeach()
