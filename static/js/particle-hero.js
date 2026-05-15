(function() {
    'use strict';

    function createCircleTexture() {
        var canvas = document.createElement('canvas');
        canvas.width = 64;
        canvas.height = 64;
        var ctx = canvas.getContext('2d');
        var gradient = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
        gradient.addColorStop(0, 'rgba(255,255,255,1)');
        gradient.addColorStop(0.3, 'rgba(255,255,255,0.8)');
        gradient.addColorStop(1, 'rgba(255,255,255,0)');
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, 64, 64);
        return new THREE.CanvasTexture(canvas);
    }

    function initParticleHero(container) {
        try {
            var rect = container.getBoundingClientRect();
            var width = rect.width;
            var height = Math.max(rect.height, 400);

            var scene = new THREE.Scene();
            var camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
            camera.position.set(0, 5, 20);

            var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            renderer.setClearColor(0x000000, 0);
            renderer.setSize(width, height);
            renderer.domElement.style.position = 'absolute';
            renderer.domElement.style.top = '0';
            renderer.domElement.style.left = '0';
            renderer.domElement.style.width = '100%';
            renderer.domElement.style.height = '100%';
            renderer.domElement.style.zIndex = '0';
            renderer.domElement.style.pointerEvents = 'none';
            container.insertBefore(renderer.domElement, container.firstChild);

            var count = Math.min(10000, Math.floor((width * height) / 200));
            var geometry = new THREE.BufferGeometry();
            var pos = new Float32Array(count * 3);
            var col = new Float32Array(count * 3);

            var c1 = new THREE.Color(0x4a9eff);
            var c2 = new THREE.Color(0x7c3aed);

            for (var i = 0; i < count; i++) {
                var x = (Math.random() - 0.5) * 100;
                var z = (Math.random() - 0.5) * 100;
                pos[i * 3] = x;
                pos[i * 3 + 1] = 0;
                pos[i * 3 + 2] = z;
                var tmp = c1.clone().lerp(c2, Math.random());
                col[i * 3] = tmp.r;
                col[i * 3 + 1] = tmp.g;
                col[i * 3 + 2] = tmp.b;
            }
            geometry.setAttribute('position', new THREE.BufferAttribute(pos, 3));
            geometry.setAttribute('color', new THREE.BufferAttribute(col, 3));

            var texture = createCircleTexture();
            var material = new THREE.PointsMaterial({
                size: 0.35,
                map: texture,
                vertexColors: true,
                transparent: true,
                opacity: 0.9,
                blending: THREE.AdditiveBlending,
                depthWrite: false,
                sizeAttenuation: true
            });

            var particles = new THREE.Points(geometry, material);
            scene.add(particles);

            var mouse = { x: 0, y: 0 };
            container.addEventListener('mousemove', function(e) {
                var r = container.getBoundingClientRect();
                mouse.x = ((e.clientX - r.left) / r.width) * 2 - 1;
                mouse.y = -((e.clientY - r.top) / r.height) * 2 + 1;
            });

            var clock = new THREE.Clock();
            var origPos = new Float32Array(pos);

            function animate() {
                requestAnimationFrame(animate);
                var t = clock.getElapsedTime();
                var p = geometry.attributes.position.array;

                for (var i = 0; i < count; i++) {
                    var x = origPos[i * 3];
                    var z = origPos[i * 3 + 2];
                    var d = Math.sqrt(x * x + z * z);

                    p[i * 3 + 1] = Math.sin(x * 0.15 + t * 1.5) * 2
                        + Math.cos(z * 0.1 + t * 1.2) * 1.5
                        + Math.sin((x + z) * 0.08 + t * 0.8)
                        + Math.sin(d * 0.2 - t * 2) * 2 / (1 + d * 0.05);

                    var mx = mouse.x * 30, mz = mouse.y * 30;
                    var dx = x - mx, dz = z - mz;
                    var md = Math.sqrt(dx * dx + dz * dz);
                    if (md < 10) {
                        p[i * 3 + 1] += Math.cos(md * 0.5 - t * 3) * 3 * Math.exp(-md / 5);
                    }
                }
                geometry.attributes.position.needsUpdate = true;

                camera.position.x += (mouse.x * 5 - camera.position.x) * 0.02;
                camera.position.y += (8 + mouse.y * 3 - camera.position.y) * 0.02;
                camera.lookAt(0, 0, 0);

                particles.rotation.y = t * 0.03;
                renderer.render(scene, camera);
            }
            animate();

            var ro = new ResizeObserver(function() {
                var r = container.getBoundingClientRect();
                var w = r.width, h = Math.max(r.height, 400);
                camera.aspect = w / h;
                camera.updateProjectionMatrix();
                renderer.setSize(w, h);
            });
            ro.observe(container);
        } catch(e) {
            console.warn('Particle hero init failed:', e);
        }
    }

    function initAll() {
        var heroes = document.querySelectorAll('.hero-gradient');
        for (var i = 0; i < heroes.length; i++) {
            initParticleHero(heroes[i]);
        }
    }

    function waitForThree() {
        if (typeof THREE !== 'undefined') {
            initAll();
        } else {
            setTimeout(waitForThree, 100);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', waitForThree);
    } else {
        waitForThree();
    }
})();
