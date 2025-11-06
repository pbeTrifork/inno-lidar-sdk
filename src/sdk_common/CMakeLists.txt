
aux_source_directory(. DIR_SRCS)
aux_source_directory(converter DIR_SRCS)

target_sources(inno_client_sdk PRIVATE ${DIR_SRCS})
