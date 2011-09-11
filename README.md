# wordpress-fabfile

This is the start of a fabric script for simplifying WordPress
development.

It currently serves one purpose: with a single command it copies down my
WordPress database from my server and makes configuration changes to it.

Also, most options are hardcoded. Here are some assumptions it makes:

*   In the directory with the fabfile are two directories, `database` and
    `www`. The `www` directory contains a copy of the WordPress root. I
    keep them in sync with git over ssh. I am not using github for this
    directory since it's several projects with different maintainers 
    combined. I am using github for individual plugins.
*   The database is named `blog`.

Besides that, there are several things that need to be customized for
using it on servers other than mine.

