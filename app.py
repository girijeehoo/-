<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>STAR BREAKER | HTML5 Arcade Space Shooter</title>
  <style>
    /* ==========================================================================
       STAR BREAKER - Global Styles & Cyberpunk Arcade UI
       Zero external dependencies; ready for instant GitHub Pages deployment.
       ========================================================================== */
    :root {
      --bg-deep: #04060e;
      --neon-cyan: #00f3ff;
      --neon-blue: #3b82f6;
      --neon-pink: #ff2a85;
      --neon-amber: #ffb703;
      --neon-green: #10b981;
      --neon-purple: #a855f7;
      --panel-bg: rgba(8, 14, 30, 0.84);
      --panel-border: rgba(0, 243, 255, 0.35);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
      -webkit-touch-callout: none;
    }

    html, body {
      width: 100%;
      height: 100%;
      overflow: hidden;
      background-color: var(--bg-deep);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }

    /* Fullscreen Interactive Game Canvas */
    #gameCanvas {
      display: block;
      width: 100vw;
      height: 100vh;
      touch-action: none;
      cursor: crosshair;
    }

    /* ==========================================================================
       Heads-Up Display (HUD)
       ========================================================================== */
    .hud-layer {
      position: fixed;
      inset: 0;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: max(12px, env(safe-area-inset-top)) max(16px, env(safe-area-inset-right)) max(12px, env(safe-area-inset-bottom)) max(16px, env(safe-area-inset-left));
      z-index: 10;
    }

    .hud-top {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
      width: 100%;
    }

    .hud-group {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .hud-card {
      background: rgba(6, 11, 25, 0.72);
      border: 1px solid rgba(0, 243, 255, 0.25);
      border-radius: 10px;
      padding: 6px 12px;
      backdrop-filter: blur(6px);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.45);
    }

    .hud-label {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: var(--text-muted);
      text-transform: uppercase;
    }

    .hud-value {
      font-size: 18px;
      font-weight: 800;
      font-variant-numeric: tabular-nums;
      letter-spacing: 0.04em;
      color: var(--text-main);
      text-shadow: 0 0 10px rgba(0, 243, 255, 0.4);
    }

    .hud-value.cyan { color: var(--neon-cyan); }
    .hud-value.amber { color: var(--neon-amber); }

    .combo-badge {
      display: inline-flex;
      align-items: center;
      padding: 4px 10px;
      border-radius: 999px;
      background: linear-gradient(135deg, rgba(255, 42, 133, 0.25), rgba(168, 85, 247, 0.25));
      border: 1px solid rgba(255, 42, 133, 0.6);
      color: #ff7eb6;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.08em;
      opacity: 0;
      transform: scale(0.85);
      transition: opacity 0.2s ease, transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .combo-badge.active {
      opacity: 1;
      transform: scale(1);
    }

    /* Lives & Active Power-up Status */
    .lives-row {
      display: flex;
      align-items: center;
      gap: 5px;
      margin-top: 2px;
    }

    .life-pip {
      width: 14px;
      height: 16px;
      display: inline-block;
      transition: transform 0.2s ease, opacity 0.2s ease;
    }

    .life-pip.lost {
      opacity: 0.2;
      transform: scale(0.8);
    }

    .status-pills {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-top: 6px;
      flex-wrap: wrap;
      justify-content: flex-end;
    }

    .pill {
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      letter-spacing: 0.05em;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .pill-weapon {
      background: rgba(0, 243, 255, 0.16);
      border: 1px solid rgba(0, 243, 255, 0.5);
      color: var(--neon-cyan);
    }

    .pill-shield {
      background: rgba(16, 185, 129, 0.18);
      border: 1px solid rgba(16, 185, 129, 0.6);
      color: #34d399;
    }

    .pill-rapid {
      background: rgba(255, 183, 3, 0.18);
      border: 1px solid rgba(255, 183, 3, 0.6);
      color: var(--neon-amber);
    }

    .rapid-bar-wrap {
      width: 44px;
      height: 5px;
      background: rgba(255, 255, 255, 0.15);
      border-radius: 99px;
      overflow: hidden;
    }

    .rapid-bar-fill {
      height: 100%;
      width: 100%;
      background: var(--neon-amber);
      transition: width 0.08s linear;
    }

    /* Interactive HUD Buttons (Pause & Audio) */
    .icon-btn {
      pointer-events: auto;
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: rgba(10, 18, 38, 0.82);
      border: 1px solid rgba(0, 243, 255, 0.35);
      color: var(--text-main);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s ease;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }

    .icon-btn:hover {
      border-color: var(--neon-cyan);
      background: rgba(0, 243, 255, 0.18);
      transform: translateY(-1px);
    }

    .icon-btn:active {
      transform: scale(0.94);
    }

    /* Boss Health Bar */
    .boss-hud {
      position: fixed;
      top: 72px;
      left: 50%;
      transform: translateX(-50%) translateY(-20px);
      width: min(460px, 86vw);
      background: rgba(12, 8, 24, 0.85);
      border: 1px solid rgba(255, 42, 133, 0.6);
      border-radius: 12px;
      padding: 8px 14px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease, transform 0.3s ease;
      box-shadow: 0 0 25px rgba(255, 42, 133, 0.3);
      z-index: 12;
    }

    .boss-hud.visible {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }

    .boss-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.12em;
      color: #ff7eb6;
      margin-bottom: 5px;
    }

    .boss-bar-bg {
      width: 100%;
      height: 10px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 999px;
      overflow: hidden;
    }

    .boss-bar-fill {
      height: 100%;
      width: 100%;
      background: linear-gradient(90deg, #ff2a85, #ff7b00);
      box-shadow: 0 0 12px rgba(255, 42, 133, 0.8);
      transition: width 0.1s ease-out;
    }

    /* ==========================================================================
       Modal Overlays (Start Screen, Pause, Game Over)
       ========================================================================== */
    .overlay-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(3, 6, 16, 0.76);
      backdrop-filter: blur(8px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      z-index: 30;
      opacity: 1;
      transition: opacity 0.25s ease;
    }

    .overlay-backdrop.hidden {
      opacity: 0;
      pointer-events: none;
    }

    .modal-card {
      width: 100%;
      max-width: 440px;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 20px;
      padding: 28px 24px;
      text-align: center;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.75), 0 0 40px rgba(0, 243, 255, 0.15);
      animation: cardFloatIn 0.35s cubic-bezier(0.22, 1, 0.36, 1);
    }

    @keyframes cardFloatIn {
      from {
        opacity: 0;
        transform: translateY(16px) scale(0.96);
      }
      to {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }

    .game-kicker {
      display: inline-block;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.22em;
      color: var(--neon-cyan);
      background: rgba(0, 243, 255, 0.12);
      border: 1px solid rgba(0, 243, 255, 0.35);
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }

    .game-title {
      font-size: clamp(32px, 7vw, 44px);
      font-weight: 900;
      letter-spacing: 0.08em;
      line-height: 1.05;
      background: linear-gradient(135deg, #ffffff 15%, #00f3ff 55%, #a855f7 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 0 18px rgba(0, 243, 255, 0.35));
      margin-bottom: 10px;
    }

    .game-subtitle {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 20px;
    }

    .guide-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 18px;
      text-align: left;
    }

    .guide-box {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 10px 12px;
    }

    .guide-box-title {
      font-size: 11px;
      font-weight: 800;
      color: var(--neon-cyan);
      letter-spacing: 0.08em;
      margin-bottom: 4px;
    }

    .guide-box-text {
      font-size: 12px;
      color: #cbd5e1;
      line-height: 1.4;
    }

    .powerup-legend {
      display: flex;
      justify-content: center;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 22px;
    }

    .legend-chip {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 9px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #e2e8f0;
    }

    .dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      display: inline-block;
    }

    /* Primary Arcade Action Button */
    .btn-primary {
      width: 100%;
      padding: 14px 24px;
      border: none;
      border-radius: 12px;
      font-size: 16px;
      font-weight: 900;
      letter-spacing: 0.12em;
      color: #030712;
      background: linear-gradient(135deg, #00f3ff 0%, #38bdf8 50%, #818cf8 100%);
      cursor: pointer;
      box-shadow: 0 8px 25px rgba(0, 243, 255, 0.4);
      transition: transform 0.15s ease, box-shadow 0.15s ease, filter 0.15s ease;
    }

    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 32px rgba(0, 243, 255, 0.6);
      filter: brightness(1.06);
    }

    .btn-primary:active {
      transform: translateY(1px) scale(0.98);
    }

    .btn-secondary {
      width: 100%;
      margin-top: 10px;
      padding: 12px 20px;
      border-radius: 12px;
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 0.1em;
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid rgba(255, 255, 255, 0.16);
      cursor: pointer;
      transition: background 0.15s ease;
    }

    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.14);
    }

    /* Stats Summary Grid on Game Over */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      margin: 18px 0 22px;
    }

    .stat-tile {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: 12px;
      padding: 12px 10px;
    }

    .stat-tile-label {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.1em;
      color: var(--text-muted);
      margin-bottom: 4px;
    }

    .stat-tile-value {
      font-size: 22px;
      font-weight: 900;
      color: var(--text-main);
    }

    .new-record-tag {
      display: inline-block;
      margin-top: 4px;
      font-size: 10px;
      font-weight: 800;
      color: #030712;
      background: var(--neon-amber);
      padding: 2px 7px;
      border-radius: 999px;
      letter-spacing: 0.08em;
    }

    @media (max-width: 520px) {
      .hud-card {
        padding: 5px 9px;
      }
      .hud-value {
        font-size: 15px;
      }
      .guide-grid {
        grid-template-columns: 1fr;
      }
      .modal-card {
        padding: 22px 18px;
      }
    }
  </style>
</head>
<body>
  <!-- Main Interactive Space Canvas -->
  <canvas id="gameCanvas"></canvas>

  <!-- Live In-Game HUD -->
  <div class="hud-layer">
    <div class="hud-top">
      <!-- Left: Score, High Score & Combo -->
      <div class="hud-group">
        <div class="hud-card">
          <div class="hud-label">Score</div>
          <div id="hudScore" class="hud-value cyan">0</div>
        </div>
        <div class="hud-card">
          <div class="hud-label">Best</div>
          <div id="hudBest" class="hud-value amber">0</div>
        </div>
        <div id="hudCombo" class="combo-badge">COMBO x1</div>
      </div>

      <!-- Center: Wave Counter -->
      <div class="hud-card" style="text-align: center;">
        <div class="hud-label">Wave</div>
        <div id="hudWave" class="hud-value">1</div>
      </div>

      <!-- Right: Lives, Power-ups & Controls -->
      <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <div class="hud-group">
          <div class="hud-card">
            <div class="hud-label">Hull</div>
            <div id="hudLives" class="lives-row"></div>
          </div>
          <button id="btnPause" class="icon-btn" title="Pause Game (P)" aria-label="Pause Game">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <rect x="6" y="4" width="4" height="16" rx="1"></rect>
              <rect x="14" y="4" width="4" height="16" rx="1"></rect>
            </svg>
          </button>
          <button id="btnMute" class="icon-btn" title="Toggle Sound" aria-label="Toggle Sound">
            <svg id="iconSoundOn" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
              <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
              <path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path>
            </svg>
            <svg id="iconSoundOff" style="display:none;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ff2a85" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
              <line x1="23" y1="9" x2="17" y2="15"></line>
              <line x1="17" y1="9" x2="23" y2="15"></line>
            </svg>
          </button>
        </div>

        <!-- Active Upgrades & Timers -->
        <div class="status-pills">
          <span id="pillWeapon" class="pill pill-weapon">WPN LV.1</span>
          <span id="pillShield" class="pill pill-shield" style="display:none;">SHIELD</span>
          <span id="pillRapid" class="pill pill-rapid" style="display:none;">
            RAPID
            <span class="rapid-bar-wrap"><span id="rapidBarFill" class="rapid-bar-fill"></span></span>
          </span>
        </div>
      </div>
    </div>
  </div>

  <!-- Boss Health Bar (Appears every 5 Waves) -->
  <div id="bossHud" class="boss-hud">
    <div class="boss-header">
      <span id="bossName">OMEGA DREADNOUGHT</span>
      <span id="bossHpText">100%</span>
    </div>
    <div class="boss-bar-bg">
      <div id="bossBarFill" class="boss-bar-fill"></div>
    </div>
  </div>

  <!-- Start Screen Overlay -->
  <div id="startOverlay" class="overlay-backdrop">
    <div class="modal-card">
      <div class="game-kicker">ORBITAL DEFENSE PROTOCOL</div>
      <h1 class="game-title">STAR BREAKER</h1>
      <p class="game-subtitle">
        Defend the deep-space frontier against hostile fleets, interceptors, and colossal dreadnought bosses.
      </p>

      <div class="guide-grid">
        <div class="guide-box">
          <div class="guide-box-title">DESKTOP CONTROLS</div>
          <div class="guide-box-text">
            <strong>WASD / Arrows</strong> to fly<br />
            <strong>Space</strong> to fire &bull; <strong>P</strong> to pause
          </div>
        </div>
        <div class="guide-box">
          <div class="guide-box-title">TOUCH &amp; MOUSE</div>
          <div class="guide-box-text">
            <strong>Drag anywhere</strong> to pilot your starfighter with auto-fire
          </div>
        </div>
      </div>

      <div class="powerup-legend">
        <span class="legend-chip"><span class="dot" style="background:#00f3ff;"></span>[W] Weapon</span>
        <span class="legend-chip"><span class="dot" style="background:#10b981;"></span>[S] Shield</span>
        <span class="legend-chip"><span class="dot" style="background:#ffb703;"></span>[R] Rapid</span>
        <span class="legend-chip"><span class="dot" style="background:#ff2a85;"></span>[H] Hull +1</span>
      </div>

      <button id="btnStart" class="btn-primary">START MISSION</button>
    </div>
  </div>

  <!-- Pause Overlay -->
  <div id="pauseOverlay" class="overlay-backdrop hidden">
    <div class="modal-card">
      <div class="game-kicker">TACTICAL STANDBY</div>
      <h2 class="game-title" style="font-size: 32px;">SYSTEM PAUSED</h2>
      <p class="game-subtitle">Take a breather, pilot. Your starfighter is holding position.</p>
      <button id="btnResume" class="btn-primary">RESUME MISSION</button>
      <button id="btnRestartFromPause" class="btn-secondary">ABORT &amp; RESTART</button>
    </div>
  </div>

  <!-- Game Over Overlay -->
  <div id="gameOverOverlay" class="overlay-backdrop hidden">
    <div class="modal-card">
      <div class="game-kicker" style="color:#ff7eb6; border-color:rgba(255,42,133,0.45); background:rgba(255,42,133,0.14);">
        HULL BREACHED
      </div>
      <h2 class="game-title" style="font-size: 34px;">GAME OVER</h2>

      <div class="stats-grid">
        <div class="stat-tile">
          <div class="stat-tile-label">FINAL SCORE</div>
          <div id="finalScore" class="stat-tile-value" style="color:#00f3ff;">0</div>
          <div id="newRecordBadge" class="new-record-tag" style="display:none;">NEW RECORD!</div>
        </div>
        <div class="stat-tile">
          <div class="stat-tile-label">BEST SCORE</div>
          <div id="finalBest" class="stat-tile-value" style="color:#ffb703;">0</div>
        </div>
        <div class="stat-tile">
          <div class="stat-tile-label">WAVE REACHED</div>
          <div id="finalWave" class="stat-tile-value">1</div>
        </div>
        <div class="stat-tile">
          <div class="stat-tile-label">MAX COMBO</div>
          <div id="finalCombo" class="stat-tile-value" style="color:#ff7eb6;">x1</div>
        </div>
      </div>

      <button id="btnPlayAgain" class="btn-primary">PLAY AGAIN</button>
    </div>
  </div>

  <script>
    /**
     * ============================================================================
     * STAR BREAKER - Complete Single-File HTML5 Arcade Space Shooter
     * ============================================================================
     * Architecture:
     *  1. SoundEngine: Zero-dependency Web Audio API retro synthesizer
     *  2. InputManager: Unified Keyboard, Mouse & Touch drag controller
     *  3. Starfield & Nebula: Multi-layered parallax deep-space renderer
     *  4. Game Entities: Player, Bullets, Enemies (Scout, Interceptor, Cruiser, Boss),
     *     PowerUps ([W], [S], [R], [H]), Particles, and Floating Popups
     *  5. GameEngine: Fixed-timestep-safe delta loop, wave director, collision solver,
     *     HUD synchronization, and localStorage persistence
     */

    (function () {
      'use strict';

      /* ==========================================================================
         1. WEB AUDIO API SYNTHESIZER (Retro Arcade SFX without external files)
         ========================================================================== */
      class SoundEngine {
        constructor() {
          this.ctx = null;
          this.muted = false;
          try {
            const savedMute = localStorage.getItem('star_breaker_muted');
            if (savedMute === 'true') this.muted = true;
          } catch (e) {
            // Ignore storage access errors in restricted frames
          }
        }

        init() {
          if (this.ctx) {
            if (this.ctx.state === 'suspended') {
              this.ctx.resume().catch(() => {});
            }
            return;
          }
          try {
            const AudioCtx = window.AudioContext || window.webkitAudioContext;
            if (AudioCtx) {
              this.ctx = new AudioCtx();
            }
          } catch (e) {
            this.ctx = null;
          }
        }

        toggleMute() {
          this.muted = !this.muted;
          try {
            localStorage.setItem('star_breaker_muted', String(this.muted));
          } catch (e) {}
          return this.muted;
        }

        playLaser(weaponLevel = 1) {
          if (this.muted || !this.ctx) return;
          try {
            const now = this.ctx.currentTime;
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();

            osc.type = weaponLevel >= 3 ? 'sawtooth' : 'square';
            const baseFreq = 680 + weaponLevel * 70 + (Math.random() * 40 - 20);
            osc.frequency.setValueAtTime(baseFreq, now);
            osc.frequency.exponentialRampToValueAtTime(160, now + 0.09);

            gain.gain.setValueAtTime(0.06, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.09);

            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now);
            osc.stop(now + 0.095);
          } catch (e) {}
        }

        playHit() {
          if (this.muted || !this.ctx) return;
          try {
            const now = this.ctx.currentTime;
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(280, now);
            osc.frequency.exponentialRampToValueAtTime(90, now + 0.05);
            gain.gain.setValueAtTime(0.07, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now);
            osc.stop(now + 0.055);
          } catch (e) {}
        }

        playExplosion(scale = 1) {
          if (this.muted || !this.ctx) return;
          try {
            const now = this.ctx.currentTime;
            const duration = Math.min(0.65, 0.22 * scale);

            // Filtered noise burst for crunch
            const bufferSize = Math.floor(this.ctx.sampleRate * duration);
            const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bufferSize; i++) {
              data[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / bufferSize, 1.5);
            }

            const noise = this.ctx.createBufferSource();
            noise.buffer = buffer;

            const filter = this.ctx.createBiquadFilter();
            filter.type = 'lowpass';
            filter.frequency.setValueAtTime(scale > 1.5 ? 520 : 880, now);
            filter.frequency.exponentialRampToValueAtTime(90, now + duration);

            const gain = this.ctx.createGain();
            gain.gain.setValueAtTime(Math.min(0.24, 0.12 * scale), now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + duration);

            noise.connect(filter);
            filter.connect(gain);
            gain.connect(this.ctx.destination);
            noise.start(now);

            // Sub-bass thump
            const sub = this.ctx.createOscillator();
            const subGain = this.ctx.createGain();
            sub.type = 'sine';
            sub.frequency.setValueAtTime(120, now);
            sub.frequency.exponentialRampToValueAtTime(32, now + duration);
            subGain.gain.setValueAtTime(0.16, now);
            subGain.gain.exponentialRampToValueAtTime(0.001, now + duration);
            sub.connect(subGain);
            subGain.connect(this.ctx.destination);
            sub.start(now);
            sub.stop(now + duration);
          } catch (e) {}
        }

        playPowerup() {
          if (this.muted || !this.ctx) return;
          try {
            const now = this.ctx.currentTime;
            const notes = [523.25, 659.25, 783.99, 1046.5]; // C5 E5 G5 C6
            notes.forEach((freq, idx) => {
              const osc = this.ctx.createOscillator();
              const gain = this.ctx.createGain();
              osc.type = 'triangle';
              const t = now + idx * 0.055;
              osc.frequency.setValueAtTime(freq, t);
              gain.gain.setValueAtTime(0.09, t);
              gain.gain.exponentialRampToValueAtTime(0.001, t + 0.14);
              osc.connect(gain);
              gain.connect(this.ctx.destination);
              osc.start(t);
              osc.stop(t + 0.15);
            });
          } catch (e) {}
        }

        playDamage(shieldAbsorbed = false) {
          if (this.muted || !this.ctx) return;
          try {
            const now = this.ctx.currentTime;
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = shieldAbsorbed ? 'sine' : 'sawtooth';
            osc.frequency.setValueAtTime(shieldAbsorbed ? 420 : 180, now);
            osc.frequency.exponentialRampToValueAtTime(shieldAbsorbed ? 140 : 45, now + 0.28);
            gain.gain.setValueAtTime(0.16, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.28);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now);
            osc.stop(now + 0.29);
          } catch (e) {}
        }

        playBossWarning() {
          if (this.muted || !this.ctx) return;
          try {
            const now = this.ctx.currentTime;
            for (let i = 0; i < 3; i++) {
              const t = now + i * 0.26;
              const osc = this.ctx.createOscillator();
              const gain = this.ctx.createGain();
              osc.type = 'sawtooth';
              osc.frequency.setValueAtTime(220, t);
              osc.frequency.linearRampToValueAtTime(145, t + 0.2);
              gain.gain.setValueAtTime(0.11, t);
              gain.gain.exponentialRampToValueAtTime(0.001, t + 0.22);
              osc.connect(gain);
              gain.connect(this.ctx.destination);
              osc.start(t);
              osc.stop(t + 0.23);
            }
          } catch (e) {}
        }
      }

      /* ==========================================================================
         2. UNIFIED INPUT MANAGER (Keyboard + Mouse Drag + Touch Drag)
         ========================================================================== */
      class InputManager {
        constructor(canvas, onPauseToggle) {
          this.keys = {};
          this.pointerActive = false;
          this.pointerX = 0;
          this.pointerY = 0;
          this.isTouch = false;

          window.addEventListener('keydown', (e) => {
            this.keys[e.code] = true;
            if (e.code === 'KeyP' || e.code === 'Escape') {
              if (onPauseToggle) onPauseToggle();
            }
            if (['Space', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.code)) {
              e.preventDefault();
            }
          });

          window.addEventListener('keyup', (e) => {
            this.keys[e.code] = false;
          });

          // Mouse Controls
          canvas.addEventListener('mousedown', (e) => {
            if (e.button !== 0) return;
            this.pointerActive = true;
            this.isTouch = false;
            this.pointerX = e.clientX;
            this.pointerY = e.clientY;
          });

          window.addEventListener('mousemove', (e) => {
            if (!this.pointerActive) return;
            this.pointerX = e.clientX;
            this.pointerY = e.clientY;
          });

          window.addEventListener('mouseup', () => {
            this.pointerActive = false;
          });

          // Touch Controls
          canvas.addEventListener(
            'touchstart',
            (e) => {
              e.preventDefault();
              if (e.touches.length > 0) {
                this.pointerActive = true;
                this.isTouch = true;
                this.pointerX = e.touches[0].clientX;
                this.pointerY = e.touches[0].clientY;
              }
            },
            { passive: false }
          );

          canvas.addEventListener(
            'touchmove',
            (e) => {
              e.preventDefault();
              if (e.touches.length > 0) {
                this.pointerActive = true;
                this.isTouch = true;
                this.pointerX = e.touches[0].clientX;
                this.pointerY = e.touches[0].clientY;
              }
            },
            { passive: false }
          );

          canvas.addEventListener('touchend', (e) => {
            if (e.touches.length === 0) {
              this.pointerActive = false;
            }
          });
        }

        getMoveVector() {
          let dx = 0;
          let dy = 0;
          if (this.keys['ArrowLeft'] || this.keys['KeyA']) dx -= 1;
          if (this.keys['ArrowRight'] || this.keys['KeyD']) dx += 1;
          if (this.keys['ArrowUp'] || this.keys['KeyW']) dy -= 1;
          if (this.keys['ArrowDown'] || this.keys['KeyS']) dy += 1;

          if (dx !== 0 && dy !== 0) {
            const inv = 1 / Math.SQRT2;
            dx *= inv;
            dy *= inv;
          }
          return { dx, dy };
        }

        isFiring() {
          return Boolean(this.keys['Space'] || this.keys['KeyZ'] || this.pointerActive);
        }
      }

      /* ==========================================================================
         3. MAIN GAME ENGINE & PROCEDURAL RENDERER
         ========================================================================== */
      class StarBreakerGame {
        constructor() {
          this.canvas = document.getElementById('gameCanvas');
          this.ctx = this.canvas.getContext('2d');
          this.sound = new SoundEngine();

          // Viewport dimensions
          this.width = window.innerWidth;
          this.height = window.innerHeight;
          this.dpr = Math.min(window.devicePixelRatio || 1, 2);

          // Game States: 'MENU' | 'PLAYING' | 'PAUSED' | 'GAMEOVER'
          this.state = 'MENU';

          // Persistent High Score
          this.highScore = 0;
          try {
            this.highScore = parseInt(localStorage.getItem('star_breaker_highscore') || '0', 10) || 0;
          } catch (e) {
            this.highScore = 0;
          }

          // Core Stats
          this.score = 0;
          this.wave = 1;
          this.combo = 1;
          this.maxCombo = 1;
          this.comboTimer = 0;
          this.screenShake = 0;
          this.bannerText = '';
          this.bannerSubtext = '';
          this.bannerTimer = 0;

          // Entity Pools
          this.stars = [];
          this.nebulas = [];
          this.player = null;
          this.bullets = [];
          this.enemyBullets = [];
          this.enemies = [];
          this.powerups = [];
          this.particles = [];
          this.popups = [];

          // Wave Management
          this.enemiesToSpawn = [];
          this.spawnTimer = 0;
          this.waveClearDelay = 0;
          this.activeBoss = null;

          // Bind UI & Input
          this.input = new InputManager(this.canvas, () => this.togglePause());
          this.bindUI();
          this.resize();
          this.initBackground();
          this.updateMuteIcons();
          this.syncHUD();

          window.addEventListener('resize', () => this.resize());
          document.addEventListener('visibilitychange', () => {
            if (document.hidden && this.state === 'PLAYING') {
              this.pauseGame();
            }
          });

          this.lastTime = performance.now();
        }

        bindUI() {
          const startAction = () => {
            this.sound.init();
            this.startNewGame();
          };

          document.getElementById('btnStart').addEventListener('click', startAction);
          document.getElementById('btnPlayAgain').addEventListener('click', startAction);
          document.getElementById('btnPause').addEventListener('click', () => this.togglePause());
          document.getElementById('btnResume').addEventListener('click', () => this.resumeGame());
          document.getElementById('btnRestartFromPause').addEventListener('click', () => {
            document.getElementById('pauseOverlay').classList.add('hidden');
            this.startNewGame();
          });

          document.getElementById('btnMute').addEventListener('click', () => {
            this.sound.init();
            this.sound.toggleMute();
            this.updateMuteIcons();
          });
        }

        updateMuteIcons() {
          const onIcon = document.getElementById('iconSoundOn');
          const offIcon = document.getElementById('iconSoundOff');
          if (this.sound.muted) {
            onIcon.style.display = 'none';
            offIcon.style.display = 'block';
          } else {
            onIcon.style.display = 'block';
            offIcon.style.display = 'none';
          }
        }

        resize() {
          this.width = window.innerWidth;
          this.height = window.innerHeight;
          this.dpr = Math.min(window.devicePixelRatio || 1, 2);
          this.canvas.width = Math.floor(this.width * this.dpr);
          this.canvas.height = Math.floor(this.height * this.dpr);
          this.ctx.setTransform(this.dpr, 0, 0, this.dpr, 0, 0);

          if (this.player) {
            this.player.x = Math.max(28, Math.min(this.width - 28, this.player.x));
            this.player.y = Math.max(60, Math.min(this.height - 36, this.player.y));
          }
        }

        initBackground() {
          // Parallax Starfields (3 distinct depth layers)
          const starCount = Math.min(160, Math.floor((this.width * this.height) / 7500));
          this.stars = [];
          for (let i = 0; i < starCount; i++) {
            const layer = i % 3; // 0: distant, 1: mid, 2: close fast
            this.stars.push({
              x: Math.random() * this.width,
              y: Math.random() * this.height,
              size: layer === 0 ? 1.1 : layer === 1 ? 1.8 : 2.5,
              speed: layer === 0 ? 24 : layer === 1 ? 65 : 145,
              alpha: layer === 0 ? 0.35 : layer === 1 ? 0.65 : 0.9,
              twinklePhase: Math.random() * Math.PI * 2,
              tint: layer === 2 && Math.random() > 0.65 ? '#7dd3fc' : '#ffffff'
            });
          }

          // Subtle Deep-Space Nebula Glows
          this.nebulas = [
            { x: this.width * 0.25, y: this.height * 0.3, r: Math.max(240, this.width * 0.32), color: 'rgba(29, 78, 216, 0.11)', vy: 8 },
            { x: this.width * 0.78, y: this.height * 0.65, r: Math.max(260, this.width * 0.35), color: 'rgba(126, 34, 206, 0.09)', vy: 11 },
            { x: this.width * 0.5, y: this.height * 0.1, r: Math.max(200, this.width * 0.28), color: 'rgba(6, 182, 212, 0.07)', vy: 6 }
          ];
        }

        startNewGame() {
          document.getElementById('startOverlay').classList.add('hidden');
          document.getElementById('pauseOverlay').classList.add('hidden');
          document.getElementById('gameOverOverlay').classList.add('hidden');
          document.getElementById('bossHud').classList.remove('visible');

          this.score = 0;
          this.wave = 1;
          this.combo = 1;
          this.maxCombo = 1;
          this.comboTimer = 0;
          this.screenShake = 0;

          this.bullets = [];
          this.enemyBullets = [];
          this.enemies = [];
          this.powerups = [];
          this.particles = [];
          this.popups = [];
          this.activeBoss = null;

          this.player = {
            x: this.width * 0.5,
            y: this.height - 95,
            vx: 0,
            vy: 0,
            radius: 18,
            speed: 440,
            tilt: 0,
            lives: 3,
            maxLives: 5,
            weaponLevel: 1,
            shield: false,
            rapidTimer: 0,
            rapidMax: 8.0,
            fireCooldown: 0,
            invulnTimer: 1.5,
            thrusterPhase: 0
          };

          this.state = 'PLAYING';
          this.setupWave(1);
          this.syncHUD();
        }

        togglePause() {
          if (this.state === 'PLAYING') {
            this.pauseGame();
          } else if (this.state === 'PAUSED') {
            this.resumeGame();
          }
        }

        pauseGame() {
          if (this.state !== 'PLAYING') return;
          this.state = 'PAUSED';
          document.getElementById('pauseOverlay').classList.remove('hidden');
        }

        resumeGame() {
          if (this.state !== 'PAUSED') return;
          this.state = 'PLAYING';
          this.lastTime = performance.now();
          document.getElementById('pauseOverlay').classList.add('hidden');
        }

        triggerGameOver() {
          this.state = 'GAMEOVER';
          document.getElementById('bossHud').classList.remove('visible');

          let isNewRecord = false;
          if (this.score > this.highScore) {
            this.highScore = this.score;
            isNewRecord = true;
            try {
              localStorage.setItem('star_breaker_highscore', String(this.highScore));
            } catch (e) {}
          }

          document.getElementById('finalScore').textContent = this.score.toLocaleString();
          document.getElementById('finalBest').textContent = this.highScore.toLocaleString();
          document.getElementById('finalWave').textContent = this.wave;
          document.getElementById('finalCombo').textContent = 'x' + this.maxCombo;
          document.getElementById('newRecordBadge').style.display = isNewRecord ? 'inline-block' : 'none';

          this.syncHUD();
          document.getElementById('gameOverOverlay').classList.remove('hidden');
        }

        /* ========================================================================
           WAVE DIRECTOR & ENEMY SPAWNING
           ======================================================================== */
        setupWave(waveNum) {
          this.wave = waveNum;
          this.enemiesToSpawn = [];
          this.spawnTimer = 0.6;
          this.activeBoss = null;

          const isBossWave = waveNum % 5 === 0;

          if (isBossWave) {
            this.showBanner(`WARNING: WAVE ${waveNum}`, 'DREADNOUGHT CLASS DETECTED');
            this.sound.playBossWarning();
            this.enemiesToSpawn.push({ type: 'boss', delay: 1.6 });
            // Escort scouts
            const escorts = Math.min(6, 2 + Math.floor(waveNum / 5) * 2);
            for (let i = 0; i < escorts; i++) {
              this.enemiesToSpawn.push({ type: 'scout', delay: 2.2 + i * 1.4 });
            }
          } else {
            this.showBanner(`WAVE ${waveNum}`, waveNum === 1 ? 'ENGAGE HOSTILE FLEET' : 'INCOMING ENEMY SQUADRON');
            const totalEnemies = 6 + waveNum * 2;
            for (let i = 0; i < totalEnemies; i++) {
              let type = 'scout';
              const roll = Math.random();
              if (waveNum >= 3 && roll > 0.72) {
                type = 'cruiser';
              } else if (waveNum >= 2 && roll > 0.42) {
                type = 'interceptor';
              }
              const interval = Math.max(0.32, 0.85 - waveNum * 0.03);
              this.enemiesToSpawn.push({ type, delay: interval });
            }
          }
          this.syncHUD();
        }

        showBanner(title, subtitle) {
          this.bannerText = title;
          this.bannerSubtext = subtitle;
          this.bannerTimer = 2.4;
        }

        spawnEnemy(type) {
          const margin = 48;
          const x = margin + Math.random() * Math.max(80, this.width - margin * 2);
          const hpScale = 1 + (this.wave - 1) * 0.14;

          if (type === 'scout') {
            this.enemies.push({
              type: 'scout',
              x,
              y: -30,
              baseX: x,
              vx: 0,
              vy: 155 + Math.min(140, this.wave * 9),
              radius: 16,
              hp: Math.ceil(1 * hpScale),
              maxHp: Math.ceil(1 * hpScale),
              score: 100,
              phase: Math.random() * Math.PI * 2,
              swayAmp: 55 + Math.random() * 45,
              swayFreq: 2.4 + Math.random() * 1.2,
              hitFlash: 0,
              fireTimer: 1.5 + Math.random() * 2.0
            });
          } else if (type === 'interceptor') {
            const dir = Math.random() > 0.5 ? 1 : -1;
            this.enemies.push({
              type: 'interceptor',
              x,
              y: -32,
              vx: dir * (175 + Math.min(110, this.wave * 7)),
              vy: 130 + Math.min(90, this.wave * 6),
              radius: 18,
              hp: Math.ceil(2 * hpScale),
              maxHp: Math.ceil(2 * hpScale),
              score: 180,
              zigTimer: 0.65,
              hitFlash: 0,
              fireTimer: 1.1 + Math.random() * 1.2
            });
          } else if (type === 'cruiser') {
            this.enemies.push({
              type: 'cruiser',
              x,
              y: -45,
              vx: (Math.random() - 0.5) * 40,
              vy: 68 + Math.min(45, this.wave * 3),
              radius: 28,
              hp: Math.ceil(6 * hpScale),
              maxHp: Math.ceil(6 * hpScale),
              score: 350,
              hitFlash: 0,
              fireTimer: 1.4,
              chargeGlow: 0
            });
          } else if (type === 'boss') {
            const bossTier = Math.floor(this.wave / 5);
            const bossHp = 95 + bossTier * 65;
            const boss = {
              type: 'boss',
              name: bossTier === 1 ? 'OMEGA DREADNOUGHT' : `VALKYRIE TITAN MK-${bossTier}`,
              x: this.width * 0.5,
              y: -90,
              targetY: Math.min(155, this.height * 0.22),
              vx: 110 + bossTier * 15,
              vy: 70,
              radius: 56,
              hp: bossHp,
              maxHp: bossHp,
              score: 2500 * bossTier,
              hitFlash: 0,
              attackTimer: 1.8,
              patternIndex: 0,
              spiralAngle: 0,
              corePhase: 0
            };
            this.enemies.push(boss);
            this.activeBoss = boss;
            document.getElementById('bossName').textContent = boss.name;
            document.getElementById('bossHud').classList.add('visible');
            this.updateBossBar();
          }
        }

        updateBossBar() {
          if (!this.activeBoss) {
            document.getElementById('bossHud').classList.remove('visible');
            return;
          }
          const pct = Math.max(0, Math.ceil((this.activeBoss.hp / this.activeBoss.maxHp) * 100));
          document.getElementById('bossBarFill').style.width = pct + '%';
          document.getElementById('bossHpText').textContent = pct + '%';
        }

        /* ========================================================================
           PLAYER WEAPONS & POWER-UPS
           ======================================================================== */
        firePlayerWeapons() {
          const p = this.player;
          if (!p) return;

          const baseCooldown = p.weaponLevel === 1 ? 0.21 : p.weaponLevel === 2 ? 0.19 : 0.17;
          p.fireCooldown = p.rapidTimer > 0 ? baseCooldown * 0.52 : baseCooldown;

          this.sound.playLaser(p.weaponLevel);

          const spawnBolt = (offsetX, offsetY, vx, vy, color, radius = 3.5, damage = 1) => {
            this.bullets.push({
              x: p.x + offsetX,
              y: p.y + offsetY,
              vx,
              vy,
              color,
              radius,
              damage
            });
          };

          const speed = -760;

          if (p.weaponLevel === 1) {
            spawnBolt(0, -22, 0, speed, '#00f3ff', 3.6, 1);
          } else if (p.weaponLevel === 2) {
            spawnBolt(-11, -16, 0, speed, '#00f3ff', 3.5, 1);
            spawnBolt(11, -16, 0, speed, '#00f3ff', 3.5, 1);
          } else if (p.weaponLevel === 3) {
            spawnBolt(0, -24, 0, speed * 1.05, '#38bdf8', 4.0, 1.2);
            spawnBolt(-14, -14, -65, speed * 0.98, '#00f3ff', 3.3, 1);
            spawnBolt(14, -14, 65, speed * 0.98, '#00f3ff', 3.3, 1);
          } else {
            // Level 4: Hyper Spread + Heavy Core Rail
            spawnBolt(-6, -24, 0, speed * 1.08, '#e0f2fe', 4.0, 1.25);
            spawnBolt(6, -24, 0, speed * 1.08, '#e0f2fe', 4.0, 1.25);
            spawnBolt(-16, -14, -120, speed * 0.96, '#00f3ff', 3.3, 1);
            spawnBolt(16, -14, 120, speed * 0.96, '#00f3ff', 3.3, 1);
            spawnBolt(-22, -8, -230, speed * 0.92, '#a855f7', 3.0, 0.9);
            spawnBolt(22, -8, 230, speed * 0.92, '#a855f7', 3.0, 0.9);
          }
        }

        maybeDropPowerup(x, y, enemyType) {
          let dropChance = 0.14;
          if (enemyType === 'interceptor') dropChance = 0.2;
          if (enemyType === 'cruiser') dropChance = 0.48;
          if (enemyType === 'boss') dropChance = 1.0;

          if (Math.random() > dropChance) return;

          // Weighted power-up selection
          const types = ['W', 'S', 'R', 'H'];
          const weights = [0.34, 0.26, 0.26, 0.14];
          let r = Math.random();
          let chosen = 'W';
          for (let i = 0; i < types.length; i++) {
            if (r < weights[i]) {
              chosen = types[i];
              break;
            }
            r -= weights[i];
          }

          const meta = {
            W: { label: 'W', color: '#00f3ff', glow: 'rgba(0, 243, 255, 0.6)' },
            S: { label: 'S', color: '#10b981', glow: 'rgba(16, 185, 129, 0.6)' },
            R: { label: 'R', color: '#ffb703', glow: 'rgba(255, 183, 3, 0.6)' },
            H: { label: 'H', color: '#ff2a85', glow: 'rgba(255, 42, 133, 0.6)' }
          }[chosen];

          this.powerups.push({
            type: chosen,
            label: meta.label,
            color: meta.color,
            glow: meta.glow,
            x,
            y,
            vy: 115,
            radius: 16,
            pulse: 0
          });
        }

        applyPowerup(pup) {
          const p = this.player;
          this.sound.playPowerup();
          this.spawnExplosion(pup.x, pup.y, pup.color, 14, 0.6);

          if (pup.type === 'W') {
            if (p.weaponLevel < 4) {
              p.weaponLevel++;
              this.addPopup(p.x, p.y - 28, `WEAPON LV.${p.weaponLevel}!`, '#00f3ff');
            } else {
              this.addScore(500);
              this.addPopup(p.x, p.y - 28, 'MAX WEAPON +500', '#00f3ff');
            }
          } else if (pup.type === 'S') {
            if (!p.shield) {
              p.shield = true;
              this.addPopup(p.x, p.y - 28, 'ENERGY SHIELD ON!', '#34d399');
            } else {
              this.addScore(400);
              this.addPopup(p.x, p.y - 28, 'SHIELD CHARGE +400', '#34d399');
            }
          } else if (pup.type === 'R') {
            p.rapidTimer = p.rapidMax;
            this.addPopup(p.x, p.y - 28, 'RAPID OVERDRIVE!', '#ffb703');
          } else if (pup.type === 'H') {
            if (p.lives < p.maxLives) {
              p.lives++;
              this.addPopup(p.x, p.y - 28, 'HULL REPAIRED +1', '#ff7eb6');
            } else {
              this.addScore(500);
              this.addPopup(p.x, p.y - 28, 'FULL HULL +500', '#ff7eb6');
            }
          }

          this.syncHUD();
        }

        /* ========================================================================
           SCORING, COMBO, PARTICLES & POPUPS
           ======================================================================== */
        addScore(basePoints, popupX = null, popupY = null) {
          const earned = Math.round(basePoints * this.combo);
          this.score += earned;
          if (this.score > this.highScore) {
            this.highScore = this.score;
          }
          if (popupX !== null && popupY !== null) {
            const label = this.combo > 1 ? `+${earned} (x${this.combo})` : `+${earned}`;
            this.addPopup(popupX, popupY, label, this.combo >= 4 ? '#ffb703' : '#f8fafc');
          }
        }

        incrementCombo() {
          this.combo = Math.min(10, this.combo + 1);
          if (this.combo > this.maxCombo) {
            this.maxCombo = this.combo;
          }
          this.comboTimer = 3.6;
        }

        addPopup(x, y, text, color = '#ffffff') {
          this.popups.push({
            x,
            y,
            text,
            color,
            vy: -48,
            life: 0.95,
            maxLife: 0.95
          });
        }

        spawnExplosion(x, y, color, count = 20, scale = 1) {
          // Shockwave ring
          this.particles.push({
            type: 'ring',
            x,
            y,
            radius: 4,
            maxRadius: 34 * scale,
            color,
            life: 0.32,
            maxLife: 0.32
          });

          // Glowing sparks & debris
          for (let i = 0; i < count; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = (60 + Math.random() * 240) * Math.sqrt(scale);
            const life = 0.28 + Math.random() * 0.42;
            this.particles.push({
              type: 'spark',
              x,
              y,
              vx: Math.cos(angle) * speed,
              vy: Math.sin(angle) * speed,
              size: (1.8 + Math.random() * 3) * Math.min(1.6, scale),
              color: i % 3 === 0 ? '#ffffff' : color,
              life,
              maxLife: life
            });
          }
        }

        damagePlayer() {
          const p = this.player;
          if (!p || p.invulnTimer > 0) return;

          if (p.shield) {
            // Shield absorbs hit and clears nearby enemy bullets
            p.shield = false;
            p.invulnTimer = 1.2;
            this.screenShake = 10;
            this.sound.playDamage(true);
            this.spawnExplosion(p.x, p.y, '#10b981', 26, 1.4);
            this.addPopup(p.x, p.y - 25, 'SHIELD ABSORBED!', '#34d399');
            this.enemyBullets = this.enemyBullets.filter(
              (b) => Math.hypot(b.x - p.x, b.y - p.y) > 160
            );
            this.syncHUD();
            return;
          }

          // Hull Hit
          p.lives--;
          p.invulnTimer = 2.0;
          if (p.weaponLevel > 1) p.weaponLevel--;
          this.combo = 1;
          this.comboTimer = 0;
          this.screenShake = 18;
          this.sound.playDamage(false);
          this.spawnExplosion(p.x, p.y, '#ff2a85', 34, 1.5);
          this.addPopup(p.x, p.y - 28, 'HULL DAMAGED!', '#ff2a85');
          this.syncHUD();

          if (p.lives <= 0) {
            this.spawnExplosion(p.x, p.y, '#ffb703', 55, 2.2);
            this.sound.playExplosion(2.0);
            this.triggerGameOver();
          }
        }

        /* ========================================================================
           MAIN SIMULATION UPDATE STEP
           ======================================================================== */
        update(dt) {
          // Always animate deep-space background for lively menu & gameplay
          this.updateBackground(dt);

          if (this.state !== 'PLAYING') return;

          // Decay screen shake & wave banners
          if (this.screenShake > 0) {
            this.screenShake = Math.max(0, this.screenShake - dt * 42);
          }
          if (this.bannerTimer > 0) {
            this.bannerTimer = Math.max(0, this.bannerTimer - dt);
          }

          // Combo decay
          if (this.combo > 1) {
            this.comboTimer -= dt;
            if (this.comboTimer <= 0) {
              this.combo = 1;
              this.syncHUD();
            }
          }

          // Wave Spawner
          if (this.enemiesToSpawn.length > 0) {
            this.spawnTimer -= dt;
            if (this.spawnTimer <= 0) {
              const next = this.enemiesToSpawn.shift();
              this.spawnEnemy(next.type);
              this.spawnTimer = this.enemiesToSpawn.length > 0 ? this.enemiesToSpawn[0].delay : 0;
            }
          } else if (this.enemies.length === 0) {
            this.waveClearDelay += dt;
            if (this.waveClearDelay >= 1.1) {
              this.waveClearDelay = 0;
              this.setupWave(this.wave + 1);
            }
          }

          this.updatePlayer(dt);
          this.updateBullets(dt);
          this.updateEnemies(dt);
          this.updatePowerups(dt);
          this.updateParticlesAndPopups(dt);
          this.syncHUD();
        }

        updateBackground(dt) {
          const warpBoost = this.state === 'PLAYING' && this.enemies.length === 0 ? 1.8 : 1.0;

          for (const neb of this.nebulas) {
            neb.y += neb.vy * dt * warpBoost;
            if (neb.y - neb.r > this.height) {
              neb.y = -neb.r;
              neb.x = Math.random() * this.width;
            }
          }

          for (const star of this.stars) {
            star.y += star.speed * dt * warpBoost;
            star.twinklePhase += dt * 3.5;
            if (star.y > this.height + 4) {
              star.y = -4;
              star.x = Math.random() * this.width;
            }
          }
        }

        updatePlayer(dt) {
          const p = this.player;
          if (!p) return;

          if (p.invulnTimer > 0) p.invulnTimer = Math.max(0, p.invulnTimer - dt);
          if (p.rapidTimer > 0) p.rapidTimer = Math.max(0, p.rapidTimer - dt);
          if (p.fireCooldown > 0) p.fireCooldown = Math.max(0, p.fireCooldown - dt);
          p.thrusterPhase += dt * 28;

          const prevX = p.x;

          if (this.input.pointerActive) {
            // Smooth responsive follow toward mouse/touch pointer (with finger offset on touch)
            const offsetY = this.input.isTouch ? -48 : 0;
            const targetX = this.input.pointerX;
            const targetY = this.input.pointerY + offsetY;
            const lerpFactor = Math.min(1, dt * 18);
            p.x += (targetX - p.x) * lerpFactor;
            p.y += (targetY - p.y) * lerpFactor;
          } else {
            const move = this.input.getMoveVector();
            p.x += move.dx * p.speed * dt;
            p.y += move.dy * p.speed * dt;
          }

          // Clamp inside playfield bounds
          const padX = 24;
          const padTop = 58;
          const padBottom = 32;
          p.x = Math.max(padX, Math.min(this.width - padX, p.x));
          p.y = Math.max(padTop, Math.min(this.height - padBottom, p.y));

          // Smooth banking tilt based on horizontal velocity
          const velX = (p.x - prevX) / Math.max(0.001, dt);
          const targetTilt = Math.max(-1, Math.min(1, velX / 420));
          p.tilt += (targetTilt - p.tilt) * Math.min(1, dt * 14);

          // Weapons firing
          if (this.input.isFiring() && p.fireCooldown <= 0) {
            this.firePlayerWeapons();
          }
        }

        updateBullets(dt) {
          // Player projectiles
          for (let i = this.bullets.length - 1; i >= 0; i--) {
            const b = this.bullets[i];
            b.x += b.vx * dt;
            b.y += b.vy * dt;

            if (b.y < -30 || b.x < -30 || b.x > this.width + 30) {
              this.bullets.splice(i, 1);
            }
          }

          // Enemy projectiles
          const p = this.player;
          for (let i = this.enemyBullets.length - 1; i >= 0; i--) {
            const eb = this.enemyBullets[i];
            eb.x += eb.vx * dt;
            eb.y += eb.vy * dt;

            if (eb.y > this.height + 30 || eb.y < -40 || eb.x < -40 || eb.x > this.width + 40) {
              this.enemyBullets.splice(i, 1);
              continue;
            }

            // Check collision against player
            if (p && Math.hypot(eb.x - p.x, eb.y - p.y) < eb.radius + p.radius * 0.72) {
              this.enemyBullets.splice(i, 1);
              this.damagePlayer();
            }
          }
        }

        updateEnemies(dt) {
          const p = this.player;

          for (let i = this.enemies.length - 1; i >= 0; i--) {
            const e = this.enemies[i];
            if (e.hitFlash > 0) e.hitFlash = Math.max(0, e.hitFlash - dt * 6);

            // Movement & AI behaviors per enemy class
            if (e.type === 'scout') {
              e.phase += e.swayFreq * dt;
              e.y += e.vy * dt;
              e.x = e.baseX + Math.sin(e.phase) * e.swayAmp;
              e.x = Math.max(26, Math.min(this.width - 26, e.x));

              e.fireTimer -= dt;
              if (e.fireTimer <= 0 && e.y > 40 && e.y < this.height * 0.65) {
                e.fireTimer = 2.6 + Math.random() * 1.5;
                this.enemyBullets.push({
                  x: e.x,
                  y: e.y + 14,
                  vx: 0,
                  vy: 260 + this.wave * 8,
                  radius: 4.5,
                  color: '#fb7185'
                });
              }
            } else if (e.type === 'interceptor') {
              e.zigTimer -= dt;
              if (e.zigTimer <= 0) {
                e.zigTimer = 0.55 + Math.random() * 0.35;
                e.vx = -e.vx;
              }
              e.x += e.vx * dt;
              e.y += e.vy * dt;

              if (e.x < 28) {
                e.x = 28;
                e.vx = Math.abs(e.vx);
              } else if (e.x > this.width - 28) {
                e.x = this.width - 28;
                e.vx = -Math.abs(e.vx);
              }

              e.fireTimer -= dt;
              if (e.fireTimer <= 0 && e.y > 30 && e.y < this.height * 0.7 && p) {
                e.fireTimer = 1.9;
                const angle = Math.atan2(p.y - e.y, p.x - e.x);
                const spd = 290 + this.wave * 8;
                this.enemyBullets.push({
                  x: e.x,
                  y: e.y + 14,
                  vx: Math.cos(angle) * spd,
                  vy: Math.sin(angle) * spd,
                  radius: 4.5,
                  color: '#c084fc'
                });
              }
            } else if (e.type === 'cruiser') {
              e.x += e.vx * dt;
              e.y += e.vy * dt;
              if (e.x < 40 || e.x > this.width - 40) e.vx = -e.vx;

              e.fireTimer -= dt;
              e.chargeGlow = e.fireTimer < 0.45 ? 1 - e.fireTimer / 0.45 : 0;

              if (e.fireTimer <= 0 && e.y > 30 && e.y < this.height * 0.72 && p) {
                e.fireTimer = 2.3;
                const baseAngle = Math.atan2(p.y - e.y, p.x - e.x);
                const spd = 250 + this.wave * 7;
                [-0.18, 0, 0.18].forEach((offset) => {
                  this.enemyBullets.push({
                    x: e.x,
                    y: e.y + 20,
                    vx: Math.cos(baseAngle + offset) * spd,
                    vy: Math.sin(baseAngle + offset) * spd,
                    radius: 5.5,
                    color: '#fbbf24'
                  });
                });
              }
            } else if (e.type === 'boss') {
              e.corePhase += dt * 4;
              if (e.y < e.targetY) {
                e.y += e.vy * dt;
              } else {
                e.x += e.vx * dt;
                if (e.x < 75) {
                  e.x = 75;
                  e.vx = Math.abs(e.vx);
                } else if (e.x > this.width - 75) {
                  e.x = this.width - 75;
                  e.vx = -Math.abs(e.vx);
                }
              }

              e.attackTimer -= dt;
              if (e.attackTimer <= 0 && e.y >= e.targetY - 10) {
                this.fireBossPattern(e);
              }
            }

            // Remove enemy if it exits bottom of screen
            if (e.y > this.height + 70 && e.type !== 'boss') {
              this.enemies.splice(i, 1);
              continue;
            }

            // Player bullets hitting enemy
            let destroyed = false;
            for (let j = this.bullets.length - 1; j >= 0; j--) {
              const b = this.bullets[j];
              if (Math.hypot(b.x - e.x, b.y - e.y) < e.radius + b.radius) {
                this.bullets.splice(j, 1);
                e.hp -= b.damage;
                e.hitFlash = 1;

                // Small spark impact
                this.spawnExplosion(b.x, b.y, b.color, 4, 0.35);

                if (e.type === 'boss') {
                  this.updateBossBar();
                }

                if (e.hp <= 0) {
                  destroyed = true;
                  this.handleEnemyDestroyed(e);
                  this.enemies.splice(i, 1);
                  break;
                } else {
                  this.sound.playHit();
                }
              }
            }

            if (destroyed) continue;

            // Direct ram collision with Player
            if (p && Math.hypot(e.x - p.x, e.y - p.y) < e.radius + p.radius * 0.8) {
              this.damagePlayer();
              if (e.type !== 'boss') {
                this.spawnExplosion(e.x, e.y, '#fb7185', 18, 1);
                this.enemies.splice(i, 1);
              }
            }
          }
        }

        fireBossPattern(boss) {
          const p = this.player;
          boss.patternIndex = (boss.patternIndex + 1) % 3;

          if (boss.patternIndex === 0) {
            // Aimed 5-way fan burst
            boss.attackTimer = 1.45;
            const aim = p ? Math.atan2(p.y - boss.y, p.x - boss.x) : Math.PI / 2;
            for (let k = -2; k <= 2; k++) {
              const a = aim + k * 0.22;
              this.enemyBullets.push({
                x: boss.x,
                y: boss.y + 34,
                vx: Math.cos(a) * 280,
                vy: Math.sin(a) * 280,
                radius: 6,
                color: '#ff2a85'
              });
            }
          } else if (boss.patternIndex === 1) {
            // Radial Nova Ring
            boss.attackTimer = 1.65;
            const count = 14;
            boss.spiralAngle += 0.35;
            for (let k = 0; k < count; k++) {
              const a = boss.spiralAngle + (k / count) * Math.PI * 2;
              this.enemyBullets.push({
                x: boss.x,
                y: boss.y + 10,
                vx: Math.cos(a) * 225,
                vy: Math.sin(a) * 225,
                radius: 5.5,
                color: '#ffb703'
              });
            }
          } else {
            // Twin wing heavy plasma columns
            boss.attackTimer = 1.25;
            [-36, 36].forEach((wx) => {
              this.enemyBullets.push({
                x: boss.x + wx,
                y: boss.y + 28,
                vx: 0,
                vy: 340,
                radius: 6.5,
                color: '#38bdf8'
              });
            });
          }
        }

        handleEnemyDestroyed(e) {
          this.incrementCombo();
          this.addScore(e.score, e.x, e.y);

          if (e.type === 'boss') {
            this.activeBoss = null;
            this.updateBossBar();
            this.screenShake = 26;
            this.sound.playExplosion(2.4);
            this.spawnExplosion(e.x, e.y, '#ff2a85', 65, 2.5);
            this.spawnExplosion(e.x - 32, e.y + 15, '#ffb703', 35, 1.6);
            this.spawnExplosion(e.x + 32, e.y - 10, '#00f3ff', 35, 1.6);
            this.maybeDropPowerup(e.x - 20, e.y, 'boss');
            this.maybeDropPowerup(e.x + 20, e.y, 'boss');
          } else if (e.type === 'cruiser') {
            this.screenShake = 11;
            this.sound.playExplosion(1.5);
            this.spawnExplosion(e.x, e.y, '#ffb703', 32, 1.45);
            this.maybeDropPowerup(e.x, e.y, 'cruiser');
          } else if (e.type === 'interceptor') {
            this.screenShake = 6;
            this.sound.playExplosion(1.1);
            this.spawnExplosion(e.x, e.y, '#c084fc', 22, 1.1);
            this.maybeDropPowerup(e.x, e.y, 'interceptor');
          } else {
            this.screenShake = 4;
            this.sound.playExplosion(0.9);
            this.spawnExplosion(e.x, e.y, '#fb7185', 18, 0.95);
            this.maybeDropPowerup(e.x, e.y, 'scout');
          }
        }

        updatePowerups(dt) {
          const p = this.player;
          for (let i = this.powerups.length - 1; i >= 0; i--) {
            const pup = this.powerups[i];
            pup.y += pup.vy * dt;
            pup.pulse += dt * 6;

            // Gentle magnetic pull when close to player
            if (p) {
              const dist = Math.hypot(p.x - pup.x, p.y - pup.y);
              if (dist < 110) {
                pup.x += ((p.x - pup.x) / dist) * 180 * dt;
                pup.y += ((p.y - pup.y) / dist) * 180 * dt;
              }
              if (dist < p.radius + pup.radius + 4) {
                this.applyPowerup(pup);
                this.powerups.splice(i, 1);
                continue;
              }
            }

            if (pup.y > this.height + 30) {
              this.powerups.splice(i, 1);
            }
          }
        }

        updateParticlesAndPopups(dt) {
          for (let i = this.particles.length - 1; i >= 0; i--) {
            const pt = this.particles[i];
            pt.life -= dt;
            if (pt.life <= 0) {
              this.particles.splice(i, 1);
              continue;
            }
            if (pt.type === 'spark') {
              pt.x += pt.vx * dt;
              pt.y += pt.vy * dt;
              pt.vx *= 0.96;
              pt.vy *= 0.96;
            } else if (pt.type === 'ring') {
              const progress = 1 - pt.life / pt.maxLife;
              pt.radius = 4 + (pt.maxRadius - 4) * progress;
            }
          }

          for (let i = this.popups.length - 1; i >= 0; i--) {
            const pop = this.popups[i];
            pop.y += pop.vy * dt;
            pop.life -= dt;
            if (pop.life <= 0) {
              this.popups.splice(i, 1);
            }
          }
        }

        /* ========================================================================
           HUD SYNCHRONIZATION
           ======================================================================== */
        syncHUD() {
          document.getElementById('hudScore').textContent = this.score.toLocaleString();
          document.getElementById('hudBest').textContent = this.highScore.toLocaleString();
          document.getElementById('hudWave').textContent = this.wave;

          const comboEl = document.getElementById('hudCombo');
          if (this.combo > 1) {
            comboEl.textContent = `COMBO x${this.combo}`;
            comboEl.classList.add('active');
          } else {
            comboEl.classList.remove('active');
          }

          if (!this.player) return;

          // Lives icons
          const livesContainer = document.getElementById('hudLives');
          let html = '';
          for (let i = 0; i < this.player.maxLives; i++) {
            const active = i < this.player.lives;
            html += `<svg class="life-pip ${active ? '' : 'lost'}" viewBox="0 0 24 24" fill="${active ? '#00f3ff' : '#475569'}">
              <path d="M12 2L4 20l8-4 8 4L12 2z"/>
            </svg>`;
          }
          livesContainer.innerHTML = html;

          // Weapon & Active Buff Pills
          document.getElementById('pillWeapon').textContent = `WPN LV.${this.player.weaponLevel}`;
          document.getElementById('pillShield').style.display = this.player.shield ? 'inline-flex' : 'none';

          const rapidPill = document.getElementById('pillRapid');
          if (this.player.rapidTimer > 0) {
            rapidPill.style.display = 'inline-flex';
            const pct = Math.max(0, (this.player.rapidTimer / this.player.rapidMax) * 100);
            document.getElementById('rapidBarFill').style.width = pct + '%';
          } else {
            rapidPill.style.display = 'none';
          }
        }

        /* ========================================================================
           PROCEDURAL GRAPHICS RENDERER (CANVAS 2D)
           ======================================================================== */
        render() {
          const ctx = this.ctx;
          ctx.save();

          // Deep-Space Base Fill
          ctx.fillStyle = '#04060e';
          ctx.fillRect(0, 0, this.width, this.height);

          // Apply Subtle Screen Shake on Impacts
          if (this.screenShake > 0.2) {
            const sx = (Math.random() - 0.5) * this.screenShake;
            const sy = (Math.random() - 0.5) * this.screenShake;
            ctx.translate(sx, sy);
          }

          // 1. Render Nebulas & Multi-Layer Parallax Stars
          this.renderBackground(ctx);

          // 2. Render Power-up Orbs
          this.renderPowerups(ctx);

          // 3. Render Player Starfighter
          if (this.player && this.player.lives > 0) {
            this.renderPlayer(ctx, this.player);
          }

          // 4. Render Enemies & Bosses
          this.renderEnemies(ctx);

          // 5. Render Projectiles
          this.renderBullets(ctx);

          // 6. Render Explosions & Floating Score Popups
          this.renderParticlesAndPopups(ctx);

          // 7. Render Wave Announcement Banner
          if (this.bannerTimer > 0 && this.state === 'PLAYING') {
            this.renderBanner(ctx);
          }

          ctx.restore();
        }

        renderBackground(ctx) {
          for (const neb of this.nebulas) {
            const grad = ctx.createRadialGradient(neb.x, neb.y, 10, neb.x, neb.y, neb.r);
            grad.addColorStop(0, neb.color);
            grad.addColorStop(1, 'rgba(4, 6, 14, 0)');
            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.arc(neb.x, neb.y, neb.r, 0, Math.PI * 2);
            ctx.fill();
          }

          for (const s of this.stars) {
            const twinkle = 0.72 + Math.sin(s.twinklePhase) * 0.28;
            ctx.globalAlpha = s.alpha * twinkle;
            ctx.fillStyle = s.tint;
            ctx.beginPath();
            ctx.arc(s.x, s.y, s.size * 0.5, 0, Math.PI * 2);
            ctx.fill();
          }
          ctx.globalAlpha = 1;
        }

        renderPlayer(ctx, p) {
          // Blink during invulnerability frames
          if (p.invulnTimer > 0 && Math.floor(p.invulnTimer * 16) % 2 === 0) {
            return;
          }

          ctx.save();
          ctx.translate(p.x, p.y);

          // Banking / Horizontal Tilt Visual Effect
          const scaleX = 1 - Math.abs(p.tilt) * 0.22;
          ctx.rotate(p.tilt * 0.14);
          ctx.scale(scaleX, 1);

          // Animated Dual Plasma Thruster Flames
          const flameLen = 16 + Math.sin(p.thrusterPhase) * 6 + (p.rapidTimer > 0 ? 7 : 0);
          [-8, 8].forEach((tx) => {
            const grad = ctx.createLinearGradient(tx, 14, tx, 14 + flameLen);
            grad.addColorStop(0, '#ffffff');
            grad.addColorStop(0.35, p.rapidTimer > 0 ? '#ffb703' : '#00f3ff');
            grad.addColorStop(1, 'rgba(59, 130, 246, 0)');
            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.moveTo(tx - 4, 14);
            ctx.lineTo(tx + 4, 14);
            ctx.lineTo(tx, 14 + flameLen);
            ctx.closePath();
            ctx.fill();
          });

          // Wingtip Cannons (Visual progression with Weapon Level)
          if (p.weaponLevel >= 2) {
            ctx.fillStyle = '#38bdf8';
            ctx.fillRect(-15, -6, 3, 14);
            ctx.fillRect(12, -6, 3, 14);
          }
          if (p.weaponLevel >= 4) {
            ctx.fillStyle = '#a855f7';
            ctx.fillRect(-22, 0, 3, 12);
            ctx.fillRect(19, 0, 3, 12);
          }

          // Sleek Starfighter Swept Wings
          const hullGrad = ctx.createLinearGradient(0, -24, 0, 20);
          hullGrad.addColorStop(0, '#f8fafc');
          hullGrad.addColorStop(0.55, '#94a3b8');
          hullGrad.addColorStop(1, '#334155');

          ctx.fillStyle = hullGrad;
          ctx.beginPath();
          ctx.moveTo(0, -25);
          ctx.lineTo(9, -6);
          ctx.lineTo(25, 13);
          ctx.lineTo(22, 18);
          ctx.lineTo(8, 12);
          ctx.lineTo(5, 18);
          ctx.lineTo(-5, 18);
          ctx.lineTo(-8, 12);
          ctx.lineTo(-22, 18);
          ctx.lineTo(-25, 13);
          ctx.lineTo(-9, -6);
          ctx.closePath();
          ctx.fill();

          // Cyan Neon Wing Accent Trim
          ctx.strokeStyle = '#00f3ff';
          ctx.lineWidth = 1.6;
          ctx.beginPath();
          ctx.moveTo(-21, 13);
          ctx.lineTo(-8, -3);
          ctx.moveTo(21, 13);
          ctx.lineTo(8, -3);
          ctx.stroke();

          // Glowing Cockpit Canopy
          const canopyGrad = ctx.createLinearGradient(0, -13, 0, 5);
          canopyGrad.addColorStop(0, '#00f3ff');
          canopyGrad.addColorStop(1, '#1d4ed8');
          ctx.fillStyle = canopyGrad;
          ctx.beginPath();
          ctx.ellipse(0, -4, 4.2, 9.5, 0, 0, Math.PI * 2);
          ctx.fill();

          ctx.restore();

          // Energy Shield Bubble
          if (p.shield) {
            ctx.save();
            ctx.translate(p.x, p.y);
            const pulse = 1 + Math.sin(performance.now() * 0.008) * 0.05;
            const r = 30 * pulse;
            const sGrad = ctx.createRadialGradient(0, 0, r * 0.55, 0, 0, r);
            sGrad.addColorStop(0, 'rgba(16, 185, 129, 0.04)');
            sGrad.addColorStop(0.85, 'rgba(16, 185, 129, 0.25)');
            sGrad.addColorStop(1, 'rgba(52, 211, 153, 0.75)');
            ctx.fillStyle = sGrad;
            ctx.beginPath();
            ctx.arc(0, 0, r, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
          }
        }

        renderEnemies(ctx) {
          for (const e of this.enemies) {
            ctx.save();
            ctx.translate(e.x, e.y);

            if (e.type === 'scout') {
              // Fast Crimson Scout Dart
              ctx.fillStyle = e.hitFlash > 0 ? '#ffffff' : '#f43f5e';
              ctx.beginPath();
              ctx.moveTo(0, 18);
              ctx.lineTo(16, -12);
              ctx.lineTo(6, -8);
              ctx.lineTo(0, -16);
              ctx.lineTo(-6, -8);
              ctx.lineTo(-16, -12);
              ctx.closePath();
              ctx.fill();

              ctx.fillStyle = '#ffe4e6';
              ctx.beginPath();
              ctx.arc(0, 2, 3.5, 0, Math.PI * 2);
              ctx.fill();
            } else if (e.type === 'interceptor') {
              // Violet Twin-Blade Zig-Zagger
              ctx.fillStyle = e.hitFlash > 0 ? '#ffffff' : '#a855f7';
              ctx.beginPath();
              ctx.moveTo(0, 20);
              ctx.lineTo(8, 4);
              ctx.lineTo(20, -14);
              ctx.lineTo(10, -18);
              ctx.lineTo(0, -8);
              ctx.lineTo(-10, -18);
              ctx.lineTo(-20, -14);
              ctx.lineTo(-8, 4);
              ctx.closePath();
              ctx.fill();

              ctx.strokeStyle = '#f0abfc';
              ctx.lineWidth = 1.5;
              ctx.stroke();
            } else if (e.type === 'cruiser') {
              // Heavy Armored Dreadnought Cruiser
              ctx.fillStyle = e.hitFlash > 0 ? '#ffffff' : '#1e293b';
              ctx.strokeStyle = '#fbbf24';
              ctx.lineWidth = 2.2;
              ctx.beginPath();
              ctx.moveTo(0, 28);
              ctx.lineTo(26, 12);
              ctx.lineTo(30, -14);
              ctx.lineTo(14, -26);
              ctx.lineTo(-14, -26);
              ctx.lineTo(-30, -14);
              ctx.lineTo(-26, 12);
              ctx.closePath();
              ctx.fill();
              ctx.stroke();

              // Plasma Reactor Core
              ctx.fillStyle = e.chargeGlow > 0 ? '#ffffff' : '#f59e0b';
              ctx.beginPath();
              ctx.arc(0, 2, 8 + e.chargeGlow * 4, 0, Math.PI * 2);
              ctx.fill();

              // Mini Health Bar above damaged cruiser
              if (e.hp < e.maxHp) {
                const bw = 38;
                ctx.fillStyle = 'rgba(0,0,0,0.6)';
                ctx.fillRect(-bw / 2, -35, bw, 4);
                ctx.fillStyle = '#fbbf24';
                ctx.fillRect(-bw / 2, -35, bw * (e.hp / e.maxHp), 4);
              }
            } else if (e.type === 'boss') {
              // Colossal Wave Boss
              ctx.fillStyle = e.hitFlash > 0 ? '#ffe4e6' : '#0f172a';
              ctx.strokeStyle = '#ff2a85';
              ctx.lineWidth = 3;

              ctx.beginPath();
              ctx.moveTo(0, 52);
              ctx.lineTo(32, 34);
              ctx.lineTo(68, 8);
              ctx.lineTo(62, -28);
              ctx.lineTo(28, -46);
              ctx.lineTo(-28, -46);
              ctx.lineTo(-62, -28);
              ctx.lineTo(-68, 8);
              ctx.lineTo(-32, 34);
              ctx.closePath();
              ctx.fill();
              ctx.stroke();

              // Inner Armored Plates
              ctx.strokeStyle = '#38bdf8';
              ctx.lineWidth = 1.8;
              ctx.strokeRect(-38, -24, 76, 36);

              // Pulsing Singularity Core
              const coreR = 15 + Math.sin(e.corePhase) * 3;
              const cGrad = ctx.createRadialGradient(0, 4, 2, 0, 4, coreR);
              cGrad.addColorStop(0, '#ffffff');
              cGrad.addColorStop(0.5, '#ff2a85');
              cGrad.addColorStop(1, 'rgba(255, 42, 133, 0)');
              ctx.fillStyle = cGrad;
              ctx.beginPath();
              ctx.arc(0, 4, coreR, 0, Math.PI * 2);
              ctx.fill();
            }

            ctx.restore();
          }
        }

        renderBullets(ctx) {
          // Player Laser Bolts
          for (const b of this.bullets) {
            ctx.save();
            ctx.fillStyle = b.color;
            ctx.shadowColor = b.color;
            ctx.shadowBlur = 10;
            ctx.beginPath();
            ctx.roundRect(b.x - b.radius * 0.75, b.y - 11, b.radius * 1.5, 22, 3);
            ctx.fill();
            ctx.restore();
          }

          // Enemy Plasma Orbs
          for (const eb of this.enemyBullets) {
            ctx.save();
            ctx.fillStyle = eb.color;
            ctx.shadowColor = eb.color;
            ctx.shadowBlur = 8;
            ctx.beginPath();
            ctx.arc(eb.x, eb.y, eb.radius, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = '#ffffff';
            ctx.beginPath();
            ctx.arc(eb.x, eb.y, eb.radius * 0.45, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
          }
        }

        renderPowerups(ctx) {
          for (const pup of this.powerups) {
            ctx.save();
            ctx.translate(pup.x, pup.y);
            const scale = 1 + Math.sin(pup.pulse) * 0.1;
            ctx.scale(scale, scale);

            // Outer Glowing Aura
            ctx.shadowColor = pup.color;
            ctx.shadowBlur = 14;
            ctx.fillStyle = 'rgba(6, 12, 28, 0.9)';
            ctx.strokeStyle = pup.color;
            ctx.lineWidth = 2.4;

            ctx.beginPath();
            ctx.arc(0, 0, pup.radius, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();

            // Letter Badge ([W], [S], [R], [H])
            ctx.shadowBlur = 0;
            ctx.fillStyle = pup.color;
            ctx.font = '900 14px sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(pup.label, 0, 1);

            ctx.restore();
          }
        }

        renderParticlesAndPopups(ctx) {
          for (const pt of this.particles) {
            const alpha = Math.max(0, pt.life / pt.maxLife);
            ctx.save();
            ctx.globalAlpha = alpha;
            if (pt.type === 'spark') {
              ctx.fillStyle = pt.color;
              ctx.beginPath();
              ctx.arc(pt.x, pt.y, pt.size, 0, Math.PI * 2);
              ctx.fill();
            } else if (pt.type === 'ring') {
              ctx.strokeStyle = pt.color;
              ctx.lineWidth = 2.5 * alpha;
              ctx.beginPath();
              ctx.arc(pt.x, pt.y, pt.radius, 0, Math.PI * 2);
              ctx.stroke();
            }
            ctx.restore();
          }

          for (const pop of this.popups) {
            const alpha = Math.min(1, (pop.life / pop.maxLife) * 1.4);
            ctx.save();
            ctx.globalAlpha = alpha;
            ctx.font = '800 13px sans-serif';
            ctx.textAlign = 'center';
            ctx.fillStyle = pop.color;
            ctx.shadowColor = 'rgba(0,0,0,0.85)';
            ctx.shadowBlur = 6;
            ctx.fillText(pop.text, pop.x, pop.y);
            ctx.restore();
          }
        }

        renderBanner(ctx) {
          const alpha = Math.min(1, this.bannerTimer * 1.5, (2.4 - this.bannerTimer) * 4);
          if (alpha <= 0) return;

          ctx.save();
          ctx.globalAlpha = alpha;
          ctx.textAlign = 'center';

          ctx.font = '900 30px sans-serif';
          ctx.fillStyle = '#ffffff';
          ctx.shadowColor = '#00f3ff';
          ctx.shadowBlur = 18;
          ctx.fillText(this.bannerText, this.width * 0.5, this.height * 0.42);

          ctx.font = '700 13px sans-serif';
          ctx.fillStyle = '#7dd3fc';
          ctx.shadowBlur = 8;
          ctx.fillText(this.bannerSubtext, this.width * 0.5, this.height * 0.42 + 26);
          ctx.restore();
        }

        /* ========================================================================
           ANIMATION LOOP
           ======================================================================== */
        loop(timestamp) {
          const rawDt = (timestamp - this.lastTime) / 1000;
          this.lastTime = timestamp;
          // Clamp dt to prevent huge jumps after tab switching
          const dt = Math.min(rawDt, 0.05);

          this.update(dt);
          this.render();

          requestAnimationFrame((t) => this.loop(t));
        }

        startLoop() {
          this.lastTime = performance.now();
          requestAnimationFrame((t) => this.loop(t));
        }
      }

      // Launch cleanly on window load
      window.onload = function () {
        const game = new StarBreakerGame();
        game.startLoop();
      };
    })();
  </script>
</body>
</html>
