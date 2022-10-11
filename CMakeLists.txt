cmake_minimum_required(VERSION 3.15)
project("tippecanoe"
    VERSION 1.34.3
    LANGUAGES C CXX
)

set(CMAKE_EXPORT_COMPILE_COMMANDS 1)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(sqlite3 CONFIG REQUIRED)
find_package(ZLIB REQUIRED)

# add_executable(tippecanoe-enumerate
#     enumerate.cpp
# )

# add_executable(tippecanoe-decode
#     decode.cpp
#     projection.cpp
#     mvt.cpp
#     write_json.cpp
#     text.cpp
#     jsonpull/jsonpull.c
#     dirtiles.cpp
# )

# add_executable(tile-join
#     tile-join.cpp
#     projection.cpp
#     mbtiles.cpp
#     mvt.cpp
#     write_json.cpp
#     evaluator.cpp
#     text.cpp
#     jsonpull/jsonpull.c
#     csv.cpp
#     dirtiles.cpp
# )


add_executable(tippecanoe
    geojson.cpp
    jsonpull/jsonpull.c
    tile.cpp
    pool.cpp
    mbtiles.cpp
    geometry.cpp
    projection.cpp
    memfile.cpp
    mvt.cpp
    serial.cpp
    main.cpp
    text.cpp
    dirtiles.cpp
    plugin.cpp
    read_json.cpp
    write_json.cpp
    geobuf.cpp
    evaluator.cpp
    geocsv.cpp
    csv.cpp
    geojson-loop.cpp
)

target_include_directories(tippecanoe PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(tippecanoe PRIVATE sqlite3 ZLIB::ZLIB)

#tippecanoe-json-tool: jsontool.o jsonpull/jsonpull.o csv.o text.o geojson-loop.o
#    $(CXX) $(PG) $(LIBS) $(FINAL_FLAGS) $(CXXFLAGS) -o $@ $^ $(LDFLAGS) -lm -lz -lsqlite3 -lpthread

