-- CrazyE Hub - GitHub Hosted Version
-- URL: https://raw.githubusercontent.com/SEU_USUARIO/CrazyEHub-Scripts/main/CrazyEHub.lua

if _G.CrazyEHubLoaded then
    return "⚠️ CrazyE Hub já está carregado!"
end

_G.CrazyEHubLoaded = true

-- Serviços
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local TweenService = game:GetService("TweenService")
local Workspace = game:GetService("Workspace")
local CoreGui = game:GetService("CoreGui")

-- Variáveis
local LocalPlayer = Players.LocalPlayer
local Camera = Workspace.CurrentCamera

-- Configurações
local Settings = {
    AimEnabled = false,
    SilentAim = false,
    ESPEnabled = false,
    NoclipEnabled = false,
    FlyEnabled = false,
    FOV = 100,
    CircleRadius = 100,
    Smoothness = 0.2,
    FlySpeed = 50
}

-- Cores
local Colors = {
    Background = Color3.fromRGB(10, 10, 15),
    Primary = Color3.fromRGB(20, 20, 25),
    Secondary = Color3.fromRGB(30, 30, 35),
    Accent = Color3.fromRGB(255, 255, 255),
    Text = Color3.fromRGB(255, 255, 255)
}

-- Criar Interface
local ScreenGui = Instance.new("ScreenGui")
ScreenGui.Parent = CoreGui
ScreenGui.Name = "CrazyEHubUI"

local MainFrame = Instance.new("Frame")
MainFrame.Parent = ScreenGui
MainFrame.Position = UDim2.new(0.3, 0, 0.25, 0)
MainFrame.Size = UDim2.new(0, 360, 0, 450)
MainFrame.BackgroundColor3 = Colors.Background
MainFrame.BorderSizePixel = 0

-- Arrastável
local TitleBar = Instance.new("TextButton")
TitleBar.Parent = MainFrame
TitleBar.Size = UDim2.new(1, 0, 0, 35)
TitleBar.BackgroundColor3 = Colors.Primary
TitleBar.Text = ""
TitleBar.AutoButtonColor = false

-- Sistema de arrastar
local dragging = false
local dragStart, startPos

TitleBar.InputBegan:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        dragging = true
        dragStart = input.Position
        startPos = MainFrame.Position
    end
end)

UserInputService.InputChanged:Connect(function(input)
    if dragging and input.UserInputType == Enum.UserInputType.MouseMovement then
        local delta = input.Position - dragStart
        MainFrame.Position = UDim2.new(
            startPos.X.Scale,
            startPos.X.Offset + delta.X,
            startPos.Y.Scale,
            startPos.Y.Offset + delta.Y
        )
    end
end)

UserInputService.InputEnded:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        dragging = false
    end
end)

-- Título
local Title = Instance.new("TextLabel")
Title.Parent = TitleBar
Title.Size = UDim2.new(1, 0, 1, 0)
Title.BackgroundTransparency = 1
Title.Text = "🔥 CRAZYE HUB 🔥"
Title.TextColor3 = Colors.Text
Title.TextSize = 18
Title.Font = Enum.Font.GothamBold

-- Área de botões
local ContentFrame = Instance.new("ScrollingFrame")
ContentFrame.Parent = MainFrame
ContentFrame.Position = UDim2.new(0, 10, 0, 50)
ContentFrame.Size = UDim2.new(1, -20, 1, -60)
ContentFrame.BackgroundTransparency = 1
ContentFrame.ScrollBarThickness = 4
ContentFrame.CanvasSize = UDim2.new(0, 0, 0, 500)

-- Funções das features
local function ToggleAimbot()
    Settings.AimEnabled = not Settings.AimEnabled
    return Settings.AimEnabled
end

local function ToggleESP()
    Settings.ESPEnabled = not Settings.ESPEnabled
    if Settings.ESPEnabled then
        for _, player in pairs(Players:GetPlayers()) do
            if player ~= LocalPlayer and player.Character then
                local highlight = Instance.new("Highlight")
                highlight.Parent = player.Character
                highlight.FillColor = Color3.fromRGB(255, 255, 255)
                highlight.FillTransparency = 0.8
            end
        end
    else
        for _, player in pairs(Players:GetPlayers()) do
            if player.Character then
                local highlight = player.Character:FindFirstChild("Highlight")
                if highlight then
                    highlight:Destroy()
                end
            end
        end
    end
    return Settings.ESPEnabled
end

local function ToggleNoclip()
    Settings.NoclipEnabled = not Settings.NoclipEnabled
    return Settings.NoclipEnabled
end

local function ToggleFly()
    Settings.FlyEnabled = not Settings.FlyEnabled
    if Settings.FlyEnabled then
        local character = LocalPlayer.Character
        if character then
            local hrp = character:FindFirstChild("HumanoidRootPart")
            if hrp then
                local bv = Instance.new("BodyVelocity")
                bv.Velocity = Vector3.new(0, 0, 0)
                bv.MaxForce = Vector3.new(10000, 10000, 10000)
                bv.Parent = hrp
                
                Workspace.Gravity = 0
            end
        end
    else
        local character = LocalPlayer.Character
        if character then
            local hrp = character:FindFirstChild("HumanoidRootPart")
            if hrp then
                for _, v in pairs(hrp:GetChildren()) do
                    if v:IsA("BodyVelocity") then
                        v:Destroy()
                    end
                end
            end
        end
        Workspace.Gravity = 196.2
    end
    return Settings.FlyEnabled
end

-- Criar botões
local buttons = {
    {"🎯 AIMBOT", ToggleAimbot},
    {"👻 ESP", ToggleESP},
    {"🚫 NOCLIP", ToggleNoclip},
    {"✈️ FLY", ToggleFly}
}

for i, btn in pairs(buttons) do
    local button = Instance.new("TextButton")
    button.Parent = ContentFrame
    button.Position = UDim2.new(0.05, 0, 0, (i-1)*45)
    button.Size = UDim2.new(0.9, 0, 0, 35)
    button.BackgroundColor3 = Colors.Button
    button.TextColor3 = Colors.Text
    button.Text = btn[1] .. ": OFF"
    button.Font = Enum.Font.Gotham
    button.TextSize = 14
    
    button.MouseButton1Click:Connect(function()
        local enabled = btn[2]()
        button.Text = btn[1] .. ": " .. (enabled and "ON" or "OFF")
    end)
end

-- Toggle UI com Delete
UserInputService.InputBegan:Connect(function(input)
    if input.KeyCode == Enum.KeyCode.Delete then
        MainFrame.Visible = not MainFrame.Visible
    end
end)

-- Noclip loop
RunService.Stepped:Connect(function()
    if Settings.NoclipEnabled then
        local character = LocalPlayer.Character
        if character then
            for _, part in pairs(character:GetDescendants()) do
                if part:IsA("BasePart") then
                    part.CanCollide = false
                end
            end
        end
    end
end)

-- Mensagem de sucesso
warn("🔥 CRAZYE HUB CARREGADO COM SUCESSO!")
warn("DELETE: Mostrar/Ocultar Interface")
warn("Clique e arraste no topo para mover")

return "✅ CrazyE Hub v1.0 - GitHub Hosted"
