# Basemaps

<style> 
    .markdown-section h3 ~ p > strong > a { color: crimson; font-size: 110%; text-decoration: none; }
    .markdown-section table { 
        margin-left:3rem; 
        width: calc(100% - 6rem); 
        border:1px solid #555;
    }
    @media (max-width: 480px) {
        .markdown-section table { 
            margin-left: 0;
            width: 100%;
        }
    }

    .markdown-section td, .markdown-section th {
        border:1px solid #555;
        padding: 8px;
        line-height: 1.2;
        line-height: 1.4;
        color: #444;

        /* These are technically the same, but use both */
        overflow-wrap: break-word;
        word-wrap: break-word;

        -ms-word-break: break-all;
        /* This is the dangerous one in WebKit, as it breaks things wherever */
        word-break: break-all;
        /* Instead use this non-standard one: */
        word-break: break-word;

        /* Adds a hyphen where the word breaks, if supported (No Blink) */
        -ms-hyphens: auto;
        -moz-hyphens: auto;
        -webkit-hyphens: auto;
        hyphens: auto;
    }
    .markdown-section th {
        background-color:#E2F0F7;
        font-weight:bold !important;
        text-align:center !important;
    }
</style>

The table below lists the basemaps recognized by Juncture.  To use these basemaps add the `basemaps=<NAMES>` attribute to the `.ve-map` tag.  Tne basemaps value is one or more basemap names.  Multiple names are comma delimited.  The first name will be the default basemap.

| Name | Min Zoom | Max Zoom |
| --------| -------- | -------- |
| CartoDB_DarkMatter |  | 20 |
| CartoDB_DarkMatterNoLabels |  | 20 |
| CartoDB_DarkMatterOnlyLabels |  | 20 |
| CartoDB_Positron |  | 20 |
| CartoDB_PositronNoLabels |  | 20 |
| CartoDB_PositronOnlyLabels |  | 20 |
| CartoDB_Voyager |  | 20 |
| CartoDB_VoyagerNoLabels |  | 20 |
| CartoDB_VoyagerOnlyLabels |  | 20 |
| CartoDB_VoyagerLabelsUnder |  | 20 |
| Esri_DeLorme | 1 | 11 |
| Esri_NatGeoWorldMap |  | 16 |
| Esri_OceanBasemap |  | 13 |
| Esri_WorldImagery |  |  |
| Esri_WorldPhysical |  | 8 |
| Esri_WorldShadedRelief |  | 13 |
| Esri_WorldStreetMap |  |  |
| Esri_WorldTerrain |  | 13 |
| Esri_WorldTopoMap |  |  |
| MtbMap |  |  |
| OpenStreetMap |  | 18 |
| OpenStreetMap_DE |  | 18 |
| OpenStreetMap_France |  | 18 |
| OpenStreetMap_HOT |  | 19 |
| OpenStreetMap_Mapnik |  | 19 |
| OpenTopoMap |  | 17 |
| OPNVKarte |  | 18 |
| Stadia_AlidadeSmooth |  | 20 |
| Stadia_AlidadeSmoothDark |  | 20 |
| Stadia_OSMBright |  | 20 |
| Stadia_Outdoors |  | 20 |
| Stamen_Terrain | 0 | 18 |
| Stamen_TerrainBackground | 0 | 18 |
| Stamen_TerrainLabels | 0 | 18 |
| Stamen_Toner | 0 | 20 |
| Stamen_TonerBackground | 0 | 20 |
| Stamen_TonerLite | 0 | 20 |
| Stamen_Watercolor | 1 | 16 |
| USGS_USTopo |  | 20 |
| USGS_USImagery |  | 20 |
| USGS_USImageryTopo |  | 20 |

<ve-snippet collapsible label="CartoDB_DarkMatter">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_DarkMatter
</ve-snippet>

<ve-snippet collapsible label="CartoDB_DarkMatterNoLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_DarkMatterNoLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_DarkMatterOnlyLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_DarkMatterOnlyLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_Positron">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_Positron
</ve-snippet>

<ve-snippet collapsible label="CartoDB_PositronNoLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_PositronNoLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_PositronOnlyLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_PositronOnlyLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_Voyager">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_Voyager
</ve-snippet>

<ve-snippet collapsible label="CartoDB_VoyagerNoLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_VoyagerNoLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_VoyagerOnlyLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_VoyagerOnlyLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_VoyagerLabelsUnder">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_VoyagerLabelsUnder
</ve-snippet>

<ve-snippet collapsible label="Esri_DeLorme">
    .ve-map Q192517 12 width=50% basemaps=Esri_DeLorme
</ve-snippet>

<ve-snippet collapsible label="Esri_NatGeoWorldMap">
    .ve-map Q192517 12 width=50% basemaps=Esri_NatGeoWorldMap
</ve-snippet>

<ve-snippet collapsible label="Esri_OceanBasemap">
    .ve-map Q192517 12 width=50% basemaps=Esri_OceanBasemap
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldGrayCanvas">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldGrayCanvas
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldImagery">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldImagery
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldPhysical">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldPhysical
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldShadedRelief">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldShadedRelief
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldStreetMap">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldStreetMap
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldTerrain">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldTerrain
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldTopoMap">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldTopoMap
</ve-snippet>

<ve-snippet collapsible label="MtbMap">
    .ve-map Q192517 12 width=50% basemaps=MtbMap
</ve-snippet>

<ve-snippet collapsible label="OpenStreetMap">
    .ve-map Q192517 12 width=50% basemaps=OpenStreetMap
</ve-snippet>

<ve-snippet collapsible label="OpenStreetMap_DE">
    .ve-map Q192517 12 width=50% basemaps=OpenStreetMap_DE
</ve-snippet>

<ve-snippet collapsible label="OpenStreetMap_France">
    .ve-map Q192517 12 width=50% basemaps=OpenStreetMap_France
</ve-snippet>

<ve-snippet collapsible label="OpenStreetMap_HOT">
    .ve-map Q192517 12 width=50% basemaps=OpenStreetMap_HOT
</ve-snippet>

<ve-snippet collapsible label="OpenStreetMap_Mapnik">
    .ve-map Q192517 12 width=50% basemaps=OpenStreetMap_Mapnik
</ve-snippet>

<ve-snippet collapsible label="OpenTopoMap">
    .ve-map Q192517 12 width=50% basemaps=OpenTopoMap
</ve-snippet>

<ve-snippet collapsible label="OPNVKarte">
    .ve-map Q192517 12 width=50% basemaps=OPNVKarte
</ve-snippet>

<ve-snippet collapsible label="Stadia_AlidadeSmooth">
    .ve-map Q192517 12 width=50% basemaps=Stadia_AlidadeSmooth
</ve-snippet>

<ve-snippet collapsible label="Stadia_AlidadeSmoothDark">
    .ve-map Q192517 12 width=50% basemaps=Stadia_AlidadeSmoothDark
</ve-snippet>

<ve-snippet collapsible label="Stadia_OSMBright">
    .ve-map Q192517 12 width=50% basemaps=Stadia_OSMBright
</ve-snippet>

<ve-snippet collapsible label="Stadia_Outdoors">
    .ve-map Q192517 12 width=50% basemaps=Stadia_Outdoors
</ve-snippet>

<ve-snippet collapsible label="Stamen_Terrain">
    .ve-map Q192517 12 width=50% basemaps=Stamen_Terrain
</ve-snippet>

<ve-snippet collapsible label="Stamen_TerrainBackground">
    .ve-map Q192517 12 width=50% basemaps=Stamen_TerrainBackground
</ve-snippet>

<ve-snippet collapsible label="Stamen_TerrainLabels">
    .ve-map Q192517 12 width=50% basemaps=Stamen_TerrainLabels
</ve-snippet>

<ve-snippet collapsible label="Stamen_Toner">
    .ve-map Q192517 12 width=50% basemaps=Stamen_Toner
</ve-snippet>

<ve-snippet collapsible label="Stamen_TonerBackground">
    .ve-map Q192517 12 width=50% basemaps=Stamen_TonerBackground
</ve-snippet>

<ve-snippet collapsible label="Stamen_TonerLite">
    .ve-map Q192517 12 width=50% basemaps=Stamen_TonerLite
</ve-snippet>

<ve-snippet collapsible label="Stamen_Watercolor">
    .ve-map Q192517 12 width=50% basemaps=Stamen_Watercolor
</ve-snippet>

<ve-snippet collapsible label="USGS_USTopo">
    .ve-map Q192517 12 width=50% basemaps=USGS_USTopo
</ve-snippet>

<ve-snippet collapsible label="USGS_USImagery">
    .ve-map Q192517 12 width=50% basemaps=USGS_USImagery
</ve-snippet>

<ve-snippet collapsible label="USGS_USImageryTopo">
    .ve-map Q192517 12 width=50% basemaps=USGS_USImageryTopo
</ve-snippet>

