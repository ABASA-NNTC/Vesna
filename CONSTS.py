class Filter:
    FIELD = 'field'
    CADASTRE = 'cadastre'
    ENTRY = 'entry'
    CAPTURE = 'capture'
    UNUSED = 'unused'
    BORDER_CAD = 'border_cad'
    BORDER_FIELD = 'border_field'

    COLOR = {FIELD: 'green', CADASTRE: 'red',
                    ENTRY: 'purple', CAPTURE: '#ff8400',
                    UNUSED: 'yellow'}

    BORDER_PROPERTIES = {BORDER_CAD: {'stroke': 'red', 'fill-opacity': 0},
                         BORDER_FIELD: {'stroke': 'cyan', 'fill-opacity': 0}
                         }

    OVERLAY_HOW = {ENTRY: 'intersection', UNUSED: 'difference', CAPTURE: 'difference'}

