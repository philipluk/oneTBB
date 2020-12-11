# -*- coding: utf-8 -*-

name = 'tbb'

version = '2019.U9-ta.1.1.0'

authors = [
    'benjamin.skinner',
]

build_requires = [
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-6']

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
    ['platform-linux', 'arch-x86_64', 'os-centos-7'],
]

build_system = 'cmake'

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.TBB_VERSION.set(split_versions[0])
    env.TBB_PACKAGE_VERSION.set(split_versions[1])

    env.TBB_ROOT.set("{root}")
    env.TBBROOT.set("{root}")
    env.TBB_ROOT_DIR.set("{root}")
    
    env.TBB_INCLUDE_DIR.set("{root}/include")
    env.TBB_LIBRARY_DIR.set("{root}/lib")

    env.PATH.append( str(env.TBB_LIBRARY_DIR) )
