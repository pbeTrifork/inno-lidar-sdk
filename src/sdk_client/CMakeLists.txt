project(innolidarsdkclient)
cmake_minimum_required(VERSION 3.0...3.28)

aux_source_directory(. DIR_SRCS)
file(GLOB_RECURSE RING_ID_SRCS "${CMAKE_CURRENT_SOURCE_DIR}/ring_id_converter/*.cpp")
list(APPEND DIR_SRCS ${RING_ID_SRCS})

target_sources(inno_client_sdk PRIVATE ${DIR_SRCS})
