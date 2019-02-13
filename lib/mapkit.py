def draw_map(grid=[20, 35, -90, 75], corners=[20, 35, -90, 75],
    delta=1, water='blue', fill='#dcbc80', res='f', **kwargs):
    from mpl_toolkits.basemap import Basemap

    m = Basemap(projection='npstere', boundinglat=grid[0], lon_0=0,
            resolution='f')
    m.drawcoastlines(linewidth=0.5)
    m.fillcontinents(color=fill, lake_color=water, zorder=0)
    m.drawstates()
    args = { 'linewidth' : .5, 'dashes' : [4,1], size : 'xx-small' }
    m.drawparallels(np.arange(grid[0], grid[1], 1, labels=[0,0,0,0], **args)
    m.drawmeridians(np.arange(grid[2], grid[3], 1, labels=[1,1,0,0], **args)
    return m

