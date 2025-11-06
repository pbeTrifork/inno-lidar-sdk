project(get_pcd)
cmake_minimum_required( VERSION 3.0...3.28 )

set(SOURCES_GET_PCD get_pcd.cpp)

add_executable(${PROJECT_NAME} ${SOURCES_GET_PCD})
target_link_libraries(${PROJECT_NAME} PRIVATE inno_client_sdk)

########################
INSTALL(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION ${PROJECT_SOURCE_DIR}/
)
