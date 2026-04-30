project(
  'minpack_numba',
  'fortran',
  version: '0.1.0',
  default_options: [
    'buildtype=release',
  ]
  )

py3 = import('python').find_installation(pure: false)

subdir('minpack_numba')

subproject('minpack',
  default_options: [
    'api=true',
    'default_library=shared',
    'python=false'
  ],
  required: true,
)
