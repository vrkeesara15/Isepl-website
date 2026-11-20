"""Inline SVG icons (24x24, stroke based)."""

def svg(paths, extra=''):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"' + extra + '>' + paths + '</svg>')

P = {
    'air': '<path d="M3 8h10a3 3 0 1 0-3-3"/><path d="M3 12h15a3 3 0 1 1-3 3"/><path d="M3 16h7"/>',
    'fire': '<path d="M12 22c4 0 7-2.8 7-7 0-3.6-2.4-5.6-3.6-8.3-.9 1.6-1.9 2.5-3 2.6.2-2.6-.6-5.2-2.6-7.3-.6 4-5.8 6.8-5.8 13 0 4.2 3.4 7 8 7z"/><path d="M12 22c-1.8 0-3-1.3-3-3 0-2 1.6-3 3-5 1.4 2 3 3 3 5 0 1.7-1.2 3-3 3z"/>',
    'water': '<path d="M12 2.8s6.5 7.2 6.5 11.7a6.5 6.5 0 0 1-13 0C5.5 10 12 2.8 12 2.8z"/><path d="M9 15a3 3 0 0 0 3 3"/>',
    'earth': '<path d="M12 21v-8"/><path d="M12 13c0-4.4 3.2-7.5 8.5-7.5 0 5-3.2 7.5-8.5 7.5z"/><path d="M12 15.5c0-3.4-2.4-6-7.5-6 0 4 2.4 6 7.5 6z"/><path d="M6 21h12"/>',
    'sky': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/>',
    'arrow': '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
    'chev': '<path d="M6 9l6 6 6-6"/>',
    'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
    'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    'pin': '<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'design': '<path d="M3 21l3.5-1 11-11-2.5-2.5-11 11L3 21z"/><path d="M14 5l2.5 2.5"/><path d="M14 21h7"/>',
    'truck': '<path d="M2 6h11v10H2z"/><path d="M13 9h4l4 4v3h-8"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    'tools': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L3 17.8V21h3.2l6.3-6.3a4 4 0 0 0 5.2-5.4l-2.6 2.6-2.5-.6-.6-2.5 2.6-2.5z"/>',
    'power': '<path d="M12 2v8"/><path d="M6.4 6.4a8 8 0 1 0 11.2 0"/>',
    'shield': '<path d="M12 22s8-3.5 8-10V5l-8-3-8 3v7c0 6.5 8 10 8 10z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    'one': '<circle cx="12" cy="12" r="9"/><path d="M8 12h8M12 8v8"/>',
    'leaf': '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.1-6"/>',
    'cert': '<circle cx="12" cy="9" r="6"/><path d="M8.5 13.8L7 22l5-3 5 3-1.5-8.2"/>',
    'panel': '<rect x="4" y="3" width="16" height="18" rx="1.5"/><path d="M8 7h8M8 11h8M8 15h3"/><circle cx="15.5" cy="15.5" r="1"/>',
    'battery': '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2"/><path d="M10 9l-2 3h4l-2 3"/>',
    'server': '<rect x="3" y="3" width="18" height="7" rx="1.5"/><rect x="3" y="14" width="18" height="7" rx="1.5"/><path d="M7 6.5h.01M7 17.5h.01M11 6.5h6M11 17.5h6"/>',
    'mist': '<path d="M12 3v4"/><path d="M8 7h8l-1 3H9z"/><path d="M7 14l-1 2M12 13v3M17 14l1 2M9 18l-1 2M15 18l1 2M12 19v2"/>',
    'detect': '<circle cx="12" cy="12" r="3"/><path d="M5.6 5.6a9 9 0 0 0 0 12.8M18.4 5.6a9 9 0 0 1 0 12.8M8.5 8.5a5 5 0 0 0 0 7M15.5 8.5a5 5 0 0 1 0 7"/>',
    'curtain': '<path d="M3 3h18"/><path d="M5 3v18M19 3v18"/><path d="M5 21c2-4 2-14 0-18M19 21c-2-4-2-14 0-18"/><path d="M9 3v18M15 3v18"/>',
    'door': '<path d="M5 21V3h14v18"/><path d="M3 21h18"/><path d="M15 12h.01"/><path d="M8 6h6v4H8z"/>',
    'valve': '<path d="M2 12h5M17 12h5"/><path d="M7 8l10 8V8L7 16z"/><path d="M12 12V5M9 5h6"/>',
    'coupling': '<rect x="7" y="6" width="10" height="12" rx="2"/><path d="M2 10h5M2 14h5M17 10h5M17 14h5"/><path d="M10 6v12M14 6v12"/>',
    'treat': '<path d="M9 3h6"/><path d="M10 3v6L5 19a1.5 1.5 0 0 0 1.4 2h11.2a1.5 1.5 0 0 0 1.4-2l-5-10V3"/><path d="M7.5 15h9"/>',
    'chem': '<path d="M9 3h6M10 3v5l-5.5 9.5A2.3 2.3 0 0 0 6.5 21h11a2.3 2.3 0 0 0 2-3.5L14 8V3"/><circle cx="10" cy="16" r="1"/><circle cx="14" cy="14" r="1"/>',
    'heat': '<path d="M14 14.8V4a2 2 0 1 0-4 0v10.8a4 4 0 1 0 4 0z"/><path d="M12 18v-6"/>',
    'roof': '<path d="M2 10l10-6 10 6"/><path d="M5 9v11h14V9"/><path d="M12 13v7"/><path d="M9 20h6"/>',
    'tank': '<ellipse cx="12" cy="5" rx="8" ry="2.5"/><path d="M4 5v13c0 1.4 3.6 2.5 8 2.5s8-1.1 8-2.5V5"/><path d="M4 12c0 1.4 3.6 2.5 8 2.5s8-1.1 8-2.5"/>',
    'channel': '<path d="M2 9h20v6H2z"/><path d="M6 9v6M10 9v6M14 9v6M18 9v6"/>',
    'grid': '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    'sensor': '<path d="M3 12h3l3-8 4 16 3-8h5"/>',
    'filter': '<path d="M3 4h18l-7 8.5V19l-4 2v-8.5z"/>',
    'house': '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
    'recover': '<path d="M3 12a9 9 0 0 1 15.5-6.3L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-15.5 6.3L3 16"/><path d="M3 21v-5h5"/>',
    'solar': '<path d="M4 20l2-9h12l2 9z"/><path d="M5 15.5h14M10 11l-1 9M14 11l1 9"/><circle cx="12" cy="5" r="2"/><path d="M12 1v.5M8 5h-.5M16.5 5H16"/>',
    'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6"/>',
    'chart': '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 6-7"/>',
}

def icon(name, extra=''):
    return svg(P[name], extra)

WA = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4z"/>'
      '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>')
